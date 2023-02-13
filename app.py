from flask import Flask, render_template,request,url_for

app = Flask(__name__)

value_mapping = {
  "network": 0.85,
  "adjacent": 0.62,
  "local": 0.55,
  "physical": 0.2,
  "low": 0.5,
  "medium": 1.0,
  "high": 1.5,
  "none": 0.0,
  "partial": 0.275,
  "complete": 0.66,
  "single": 1.0,
  "multiple": 1.5,
}

def calculate_cvss_score(base_score):
 
  if base_score >= 9.0:
    severity = "Critical"
  elif base_score >= 7.0:
    severity = "High"
  elif base_score >= 4.0:
    severity = "Medium"
  else:
    severity = "Low"
  return base_score, severity

@app.route('/',methods=['POST','GET'])

def index ():
   # return ("hello")
   if request.method=='POST': 
      access_vector = request.form["access_vector"]
      access_complexity = request.form["access_complexity"]
      authentication = request.form["authentication"]
      confidentiality_impact = request.form["confidentiality_impact"]
      integrity_impact = request.form["integrity_impact"]
      availability_impact = request.form["availability_impact"]

      access_vector_value = value_mapping[access_vector]
      access_complexity_value = value_mapping[access_complexity]
      authentication_value = value_mapping[authentication]
      confidentiality_impact_value = value_mapping[confidentiality_impact]
      integrity_impact_value = value_mapping[integrity_impact]
      availability_impact_value = value_mapping[availability_impact]

      base_score = 10 * (confidentiality_impact_value + integrity_impact_value + availability_impact_value) * access_complexity_value
      base_score = base_score * access_vector_value * authentication_value

      cvss_score, severity = calculate_cvss_score(base_score)

      return render_template("result.html", cvss_score=cvss_score, severity=severity)
   return render_template("cvss_1.html")

  


   
