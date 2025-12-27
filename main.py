import os
from uttils import llama
from llm import generate_recipe

print("WORKING DIRECTORY:", os.getcwd())

print("TEST IMPORT:", generate_recipe)


def show_menu():
    print("=== Recipe Generator Plus ===")
    print("1. Input bahan")
    print("2. Lihat bahan")
    print("3. Tambah bahan")
    print("4. hapus barang")
    print("5. Generate resep (AI)")
    print("6. Keluar")

def input_ingredients():
    user_input = input("Masukkan bahan (pisahkan dengan koma): ")
    ingredients = [item.strip() for item in user_input.split(",")]
    return ingredients

def save_ingredients_to_file(ingredients):
    with open("ingredients.txt","w") as file:
        for item in ingredients:
            file.write(item + "\n")
            
def load_ingredients_from_file():
    try:
        with open("ingredients.txt", "r") as file:
            ingredients = [line.strip() for line in file]
        return ingredients
    except FileNotFoundError:
        return None

def main():
    ingredients = load_ingredients_from_file() or []
    while True:
        show_menu()
        choices = input("pilih menu: 1/2/3/4 : ")
        if choices == "1":
            ingredients = input_ingredients()
            save_ingredients_to_file(ingredients)
            print("bahan kamu :",ingredients)
        elif choices == "2":
            if ingredients is None:
                print("bahan kamu kosong:")
            else:
                print("bahan kamu:",ingredients)
        elif choices == "3":
            if ingredients is None:
                print("barang kamu masih kosong input dulu di 1")
            else:
                new_items = input_ingredients()
                ingredients.extend(new_items)
                save_ingredients_to_file(ingredients)
                print("bahan sekarang:",ingredients)
        elif choices == "4":
            if ingredients is None or len(ingredients) == 0:
                print("tidak ada barang yang bisa dihapus karena kosong")
            else:
                remove_items = input_ingredients()
                
                for item in remove_items:
                    if item in ingredients:
                        ingredients.remove(item)
                        print(f"{item} dihapus")
                    else:
                        print(f"{item} tidak ditemukan")
                save_ingredients_to_file(ingredients)
                print("bahan sekarang:",ingredients) 
        elif choices == "5":
            if not ingredients:
                print("belum ada bahan")
            else:
                print("ai sedang memuat")
                recipe =llama(ingredients)
                print("\n RESEP DARI AI")
                print(recipe)
        elif choices == "6":
            print("anda keluar!")
            break
        else :
            print("input tidak valid")
if __name__ == "__main__":
    main()
print("TEST IMPORT:", generate_recipe)



