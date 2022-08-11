Team = {
    "Top Memba" : "Al Abdulmalik",
    "Manager" : "Onimisi Kaka",
    "Director" : "Almapian",
    "Head Consultant" : "AL Aluya",
    "Clients" : {
        "Werey 1" : "Baba Emma",
        "Werey 2" : "Tomide",
        "Highest Buyer" : "Odimayo"
    }
}
print(Team.get("Top Memba"))
for key,value in Team.items() :
    print(f"{key} =====> {value}")