def calculate_cvss_score(base_score):
  # The CVSS standard defines the following severity levels for the base score:
  #   0.0 - 3.9: Low
  #   4.0 - 6.9: Medium
  #   7.0 - 8.9: High
  #   9.0 - 10.0: Critical
  if base_score >= 9.0:
    severity = "Critical"
  elif base_score >= 7.0:
    severity = "High"
  elif base_score >= 4.0:
    severity = "Medium"
  else:
    severity = "Low"
  return base_score, severity

# Define the mapping from base score factor values to numeric values
value_mapping = {
  "Network": 0.85,
  "Adjacent": 0.62,
  "Local": 0.55,
  "Physical": 0.2,
  "Low": 0.5,
  "Medium": 1.0,
  "High": 1.5,
  "None": 0.0,
  "Partial": 0.275,
  "Complete": 0.66,
  "Single": 1.0,
  "Multiple": 1.5,
}

# Prompt the user to enter the values for the base score factors
access_vector = input("Enter the access vector (Network/Adjacent/Local/Physical): ")
access_complexity = input("Enter the access complexity (Low/Medium/High): ")
authentication = input("Enter the authentication required (None/Single/Multiple): ")
confidentiality_impact = input("Enter the confidentiality impact (None/Partial/Complete): ")
integrity_impact = input("Enter the integrity impact (None/Partial/Complete): ")
availability_impact = input("Enter the availability impact (None/Partial/Complete): ")

# Assign numeric values to the base score factors based on the value mapping
access_vector_value = value_mapping[access_vector]
access_complexity_value = value_mapping[access_complexity]
authentication_value = value_mapping[authentication]
confidentiality_impact_value = value_mapping[confidentiality_impact]
integrity_impact_value = value_mapping[integrity_impact]
availability_impact_value = value_mapping[availability_impact]

# Calculate the base score
base_score = 10 * (confidentiality_impact_value + integrity_impact_value + availability_impact_value) * access_complexity_value
base_score = base_score * access_vector_value * authentication_value

# Calculate the final CVSS score and severity level
cvss_score, severity = calculate_cvss_score(base_score)

# Print the final CVSS score and severity level
print(f"CVSS score: {cvss_score:.1f} ({severity})")
