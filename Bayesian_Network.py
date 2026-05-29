# Bayesian Network Example

# Probability of Rain
P_Rain = 0.3

# Probability of Wet Grass given Rain
P_WetGrass_given_Rain = 0.9

# Probability of Wet Grass given No Rain
P_WetGrass_given_NoRain = 0.2

# Total Probability of Wet Grass
P_WetGrass = (
    P_WetGrass_given_Rain * P_Rain
    +
    P_WetGrass_given_NoRain * (1 - P_Rain)
)

print("Bayesian Network Example")
print("------------------------")
print("P(Rain) =", P_Rain)
print("P(Wet Grass | Rain) =", P_WetGrass_given_Rain)
print("P(Wet Grass | No Rain) =", P_WetGrass_given_NoRain)
print()
print("P(Wet Grass) =", round(P_WetGrass, 2))
