import ipaddress

def validate_subnet(subnet):
    """
    Valide si le sous-réseau est dans un format correct.
    """
    try:
        # Vérifie si le sous-réseau est valide
        ipaddress.IPv4Network(subnet, strict=False)
        return True, ""
    except ValueError as e:
        return False, str(e)

def calculate_supernet(subnets):
    """
    Calcule le super-réseau à partir de plusieurs sous-réseaux donnés.
    """
    # Convertir chaque sous-réseau en un objet IP Network
    networks = []
    for subnet in subnets:
        valid, message = validate_subnet(subnet)
        if not valid:
            return None, f"Erreur dans le sous-réseau {subnet} : {message}"

        networks.append(ipaddress.IPv4Network(subnet, strict=False))

    # Si les réseaux sont compatibles, on les fusionne pour obtenir le super-réseau
    try:
        supernet = networks[0]
        for network in networks[1:]:
            supernet = supernet.supernet(new_prefix=supernet.prefixlen - 1)
        return supernet, ""
    except ValueError as e:
        return None, f"Impossible de calculer le super-réseau à partir de ces sous-réseaux : {str(e)}"

def suggest_corrected_subnet(subnet):
    """
    Suggère une correction pour un sous-réseau invalide ou incompatible.
    """
    try:
        network = ipaddress.IPv4Network(subnet, strict=False)
        # Corrige l'adresse si elle est mal formée (par exemple, si l'adresse de réseau est incorrecte)
        corrected_network = network.network_address
        return f"{corrected_network}/{network.prefixlen}"
    except ValueError:
        return None

def main():
    # Demander les sous-réseaux à l'utilisateur
    print("Entrez les sous-réseaux que vous souhaitez fusionner (ex : 192.168.1.0/24) :")
    subnets_input = input("Liste des sous-réseaux séparés par des espaces : ")
    
    subnets = subnets_input.split()

    # Calculer le super-réseau
    supernet, error_message = calculate_supernet(subnets)

    if supernet:
        print(f"Le super-réseau calculé est : {supernet}")
    else:
        print(f"Erreur : {error_message}")
        
        # Essayer de suggérer des corrections
        for subnet in subnets:
            corrected_subnet = suggest_corrected_subnet(subnet)
            if corrected_subnet:
                print(f"Sugestion pour le sous-réseau '{subnet}' : {corrected_subnet}")
            else:
                print(f"Le sous-réseau '{subnet}' est invalide et nécessite une correction manuelle.")

if __name__ == "__main__":
    main()

