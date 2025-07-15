import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from Valida_Bac import validar_bac
from Valida_Campos_Obrigatorios import validar_campos_obrigatorios
from Valida_Colunas_novas import validar_colunas_novas
from Valida_ddi_telefone import validar_ddi_telefone
from Valida_Duplicatas import validar_duplicatas
from Valida_Nota import validar_nota, validar_nota_2, validar_nota_3
from ManipulaArquivo import carregar, mover_arquivo


def enviar_email(metodos_com_erro: dict, nome_arquivo: str):
    remetente = "noreply@exata.email"
    destinatario = "kaynan.baptista@exata.it"
    servidor_smtp = "10.84.22.248"
    porta = 25
    usar_auth = False  # <- seu caso
    usar_tls = False   # <- seu caso

    assunto = f"[DataQuality] arquivo NPS: validações falharam no arquivo {nome_arquivo}"

    # Corpo com todos os métodos com erro
    msg = MIMEMultipart("alternative")
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto

    # Corpo HTML
    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; font-size: 14px; color: #333;">
        <p><strong>Arquivo com erro:</strong> {nome_arquivo}</p>
        <p><strong>Validações que falharam:</strong></p>
        <ul>
    """

    for metodo, detalhes in metodos_com_erro.items():
        html += f"<li><strong>{metodo}</strong>"
        if detalhes:
            html += f"<br><span style='color: #990000;'>{detalhes}</span>"
        html += "</li>"

    html += """
        </ul>
        <p>Por favor, revise o arquivo e corrija os problemas identificados.</p>
        <p style="font-size: 12px; color: #888;">Mensagem automática do sistema de validação de dados.</p>
    </body>
    </html>
    """

    # Anexa o HTML
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP(servidor_smtp, porta) as servidor:
            if usar_tls:
                servidor.starttls()
            if usar_auth:
                servidor.login(remetente, os.getenv("EMAIL_SENHA"))
            servidor.send_message(msg)
            print(f"[✔] E-mail enviado para {destinatario}.")
    except Exception as e:
        print(f"[X] Falha ao enviar e-mail: {e}")


def main():
    pasta_origem = 'C:\\Users\\Kaynan Ribeiro\\Desktop\\Git\\Data_Quality_Homolog\\'
    pasta_destino = 'C:\\Users\\Kaynan Ribeiro\\Desktop\\Git\\Data_Quality_Homolog\\Processados'
    colunas_obrigatorias = ['TicketID', 'Data', 'Telefone', 'Dealer']
    colunas_esperadas = ['data', 'telefone', 'bac', 'dealer', 'nota', 'resposta', 'comentario', 'ticketid']

    df, caminho_arquivo, arquivo = carregar(pasta_origem)
    metodos_com_erro = {}

    # 1. validar_campos_obrigatorios
    campos_obrigatorios_resultado = validar_campos_obrigatorios(df, colunas_obrigatorias)
    campos_falhos = [campo for campo, status in campos_obrigatorios_resultado.items() if status == 1]
    if campos_falhos:
        metodos_com_erro["Algum dos campos obrigatorios não foi enviado corretamente"] = f"Campos com erro: {', '.join(campos_falhos)}"

    # 2. Demais métodos simples
    validacoes = {
        'Algum BAC não chegou preenchido': validar_bac(df),
        'Alguma coluna nova foi enviada no arquivo': validar_colunas_novas(df, colunas_esperadas),
        'Algum DDI é diferente do pais no qual o numero foi enviado': validar_ddi_telefone(df, arquivo),
        'Alguma duplicata foi encontrada no arquivo': validar_duplicatas(df),
        'Alguma nota chegou null ou vazia': validar_nota(df),
        'Alguma nota chegou com o valor maior que 10': validar_nota_2(df),
        'Alguma nota chegou com o valor menor que 0': validar_nota_3(df),
    }

    for metodo, resultado in validacoes.items():
        print(f"{metodo}: {resultado}")
        if resultado == 1:
            metodos_com_erro[metodo] = ""  # sem detalhe

    # 3. Enviar e-mail se houver algum erro
    if metodos_com_erro:
        enviar_email(metodos_com_erro, arquivo)

    # 4. Mover arquivo se carregado corretamente
    if df is not None and caminho_arquivo:
        mover_arquivo(caminho_arquivo, pasta_destino)


if __name__ == '__main__':
    main()