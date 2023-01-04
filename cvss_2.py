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

access_vector = input("Enter the access vector (Network/Adjacent/Local/Physical): ")
access_complexity = input("Enter the access complexity (Low/Medium/High): ")
authentication = input("Enter the authentication required (None/Single/Multiple): ")
confidentiality_impact = input("Enter the confidentiality impact (None/Partial/Complete): ")
integrity_impact = input("Enter the integrity impact (None/Partial/Complete): ")
availability_impact = input("Enter the availability impact (None/Partial/Complete): ")


if access_vector == "Network":
  access_vector_value = 0.85
elif access_vector == "Adjacent":
  access_vector_value = 0.62
elif access_vector == "Local":
  access_vector_value = 0.55
else:
  access_vector_value = 0.2

if access_complexity == "Low":
  access_complexity_value = 0.5
elif access_complexity == "Medium":
  access_complexity_value = 1.0
else:
  access_complexity_value = 1.5

if authentication == "None":
  authentication_value = 0.5
elif authentication == "Single":
  authentication_value = 1.0
else:
  authentication_value = 1.5

if confidentiality_impact == "None":
  confidentiality_impact_value = 0.0
elif confidentiality_impact == "Partial":
  confidentiality_impact_value = 0.275
else:
  confidentiality_impact_value = 0.66

if integrity_impact == "None":
  integrity_impact_value = 0.0
elif integrity_impact == "Partial":
  integrity_impact_value = 0.275
else:
  integrity_impact_value = 0.66

if availability_impact == "None":
  availability_impact_value = 0.0
elif availability_impact == "Partial":
  availability_impact_value = 0.275
else:
  availability_impact_value = 0.66


base_score = 10 * (confidentiality_impact_value + integrity_impact_value + availability_impact_value) * access_complexity_value
base_score = base_score * access_vector_value * authentication_value


cvss_score, severity = calculate_cvss_score(base_score)


print(f"CVSS score: {cvss_score:.1f} ({severity})")
