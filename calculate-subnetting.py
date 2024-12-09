import ipaddress

# Fonction pour réaliser du subnetting
def subnetting(network: str, new_prefix: int):
    try:
        # Créer un objet IPv4Network à partir du réseau de base
        base_network = ipaddress.IPv4Network(network, strict=False)
        
        # Diviser le réseau en sous-réseaux avec le nouveau préfixe
        subnets = list(base_network.subnets(new_prefix=new_prefix))
        
        print(f"Réseau de base: {base_network}")
        print(f"Sous-réseaux avec un préfixe /{new_prefix}:")
        for subnet in subnets:
            print(subnet)
    
    except ValueError as e:
        print(f"Erreur: {e}")

# Fonction pour réaliser du supernetting
def supernetting(networks: list, new_prefix: int):
    try:
        # Créer des objets IPv4Network à partir des réseaux fournis
        base_networks = [ipaddress.IPv4Network(net, strict=False) for net in networks]
        
        # Trouver le super-réseau qui englobe tous les réseaux
        supernet = base_networks[0].supernet(new_prefix=new_prefix)
        
        for net in base_networks[1:]:
            supernet = supernet.supernet(new_prefix=new_prefix)
        
        print(f"Super-réseau qui englobe les réseaux donnés : {supernet}")
    
    except ValueError as e:
        print(f"Erreur: {e}")

# Exemple d'utilisation du programme
if __name__ == "__main__":
    print("=== Subnetting ===")
    # Exemple de réseau de départ et division en sous-réseaux de préfixe /26
    subnetting("10.93.1.0/13", 21)
    



