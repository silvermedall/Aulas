fun main() {
    val idade: Int = 18

    if (idade >= 18) {
        println("Pode votar.")
    } else {
        println("Não pode votar.")
    }

    val nome: String = ""
    when (nome) {
        "Tiago" -> println("É o Tiago.")
        "Manuel" -> println("É o Manuel.")
        else -> println("Não é ninguém conhecido.")
    }

    when {
        4 % 2 == 0 -> println("4 é par.")
        "Tiago" != "Manuel" -> println("Diferente.")
    }
}