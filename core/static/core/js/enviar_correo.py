# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import smtplib
# from email.mime.text import MIMEText


# app = Flask(__name__)
# CORS(app)

# @app.route('/enviar_correo', methods=['POST'])
# def enviar_correo():
# 	destinatario = request.json['destinatario']
# 	asunto = request.json['asunto']
# 	mensaje = request.json['mensaje']
# 	gmail_user = 'musicproventass@gmail.com'
# 	gmail_password = 'Clavefacil1'
# 	smtp_server = 'smtp.gmail.com'
# 	smtp_port = 587
# 	server = smtplib.SMTP(smtp_server, smtp_port)
# 	server.starttls()
# 	server.login(gmail_user, gmail_password)
# 	msg = MIMEText(mensaje)
# 	msg['Subject'] = asunto
# 	msg['From'] = gmail_user
# 	msg['To'] = destinatario
# 	server.sendmail(gmail_user, destinatario, msg.as_string())
# 	server.quit()
# 	return jsonify({'status': 'ok'})

# if __name__ == '__main__':
# 	app.run()