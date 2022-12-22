
import math

impact = float(input("enter the value for impact "))
print(impact)
exploitability = float(input("enter the value exploitability "))
print(exploitability)
temporalscore = float(input("enter the value for temporalscore "))
print(temporalscore)
environmentalscore = float(input(" enter the value for environmentalscore "))
print(environmentalscore)


def cvss_score(impact, exploitability):   #base score
  return (0.6 * impact) + (0.4 * exploitability) - 1.5


def cvss_temporal_score(base_score, temporalscore): #temporal score
  return base_score * temporalscore


def cvss_environmental_score(tempscore, environmentalscore):  #environmental score
  return tempscore * environmentalscore


def round_to_tenth(score):  # round to near 10th
  return round(score * 10) / 10


def calculate_cvss_score(impact, exploitability, temporalscore, environmentalscore):  #main function to calculate cvss score

  base_score = cvss_score(impact, exploitability) #base score calculation

 
  tempscore = cvss_temporal_score(base_score, temporalscore)  #temporal score calculation

  
  environmental_score = cvss_environmental_score(tempscore, environmentalscore) #env score calculation

 
  score = round_to_tenth(environmental_score) #rounding, (final result)

  
  return score

print(calculate_cvss_score(impact, exploitability, temporalscore, environmentalscore))
