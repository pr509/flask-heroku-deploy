import openai
openai.api_key = "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"
from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route('/translation',methods=['POST'])

def translation():
  data=request.get_json()
  text=data['text']
  language=data['lang']
  model_engine = "text-davinci-003"
  prompt=f"translate to {language} :{text}"
  completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
  response = completion.choices[0].text
  ans={"translation" : response}
  return jsonify(ans)

if __name__=="__main__":
  app.run(debug=False,host='0.0.0.0')

