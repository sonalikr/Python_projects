my_cohort = ["Sapna", "Tom", "Eden", "Abdul", "Jaabir", "Lynsey", "Lauren", "Jonnah", "Sonali", "Shalini"]
counter = {}

for cohort in my_cohort:
  changed_cohort = cohort.lower()
  if changed_cohort[0] in counter:
    counter[changed_cohort[0]] = counter[changed_cohort[0]] + 1
  else:
    counter[changed_cohort[0]] = 1
    
print(counter)