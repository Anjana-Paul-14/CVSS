
import math

impact = input("enter the value for impact ")
print(impact)
exploitability = input("enter the value exploitability ")
print(exploitability)
temporalscore = float(input("enter the value for temporalscore "))
print(temporalscore)
environmentalscore = float(input(" enter the value for environmentalscore "))
print(environmentalscore)

# Define a dictionary to map the literal values to their corresponding numeric scores
score_mapping = {
  "remote": 10.0,
  "local": 7.5,
  "physical": 5.0
}


def cvss_score(impact, exploitability):
  return (0.6 * impact) + (0.4 * exploitability) - 1.5


def cvss_temporal_score(base_score, temporalscore):
  return base_score * temporalscore


def cvss_environmental_score(tempscore, environmentalscore):
  return tempscore * environmentalscore


def round_to_tenth(score):
  return round(score * 10) / 10


def calculate_cvss_score(impact, exploitability, temporalscore, environmentalscore):
    
  # Map the literal values to their corresponding numeric scores
  impact = score_mapping[impact]
  exploitability = score_mapping[exploitability]


  base_score = cvss_score(impact, exploitability)

  
  tempscore = cvss_temporal_score(base_score, temporalscore)

  
  environmental_score = cvss_environmental_score(tempscore, environmentalscore)

  
  score = round_to_tenth(environmental_score)

  
  return score


#impact = "remote"
#exploitability = "local"
#temporal_score_modifier = 1.0
#environmental_score_modifier = 0.85

print(calculate_cvss_score(impact, exploitability, temporalscoremodifier, environmentalscore))
