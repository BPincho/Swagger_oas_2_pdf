import os
from flask import (Flask, send_file, abort)
from subprocess import call, CalledProcessError

app = Flask(__name__)

@app.route('/<path:api_url>')
def downloadPdf(api_url):
	print("starting json to markup convertion \n")
	if 'version' in api_url:
		json_url = api_url.split("version")[0] + '?version' + api_url.split("version")[1]
	else:
		json_url = api_url
	try:	
		call(["java","-jar","swagger2markup-cli-1.3.3.jar","convert","-i",
			 json_url,"-f","DAA_API"])
		print("markup to pdf convertion \n")
		import pdb;pdb.set_trace()
		call(["asciidoctor-pdf", "DAA_API.adoc"])
		print("PDF Generated \n")
		path = "DAA_API.pdf"
		return send_file(path, as_attachment=True)
	except FileNotFoundError:
		return abort(418)

port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)