fun main() {
    print("Introduz o teu nome: ")
    val nome: String = readln()
    println("Olá $nome.")

    print("Introduz a tua idade: ")
    val idade: Int = readln().toInt()
    println("Tens $idade anos.")

    print("Introduz a tua altura: ")
    val altura: Double = readln().toDouble()
    println("Tens $altura metros.")
}
