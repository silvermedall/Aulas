fun main() {
    println("Insira três nomes:")
    var a: String = readln()
    var b: String = readln()
    var c: String = readln()
    println(c)
    println(b)
    println(a)

    println()

    println("Insira o salário:")
    var d: Int = readln().toInt()
    var e: Int = 920
    var f: Int = d / e
    println("O salário engloba $f salários minimos.")

    println()

    println("Insira um número com 3 dígitos:")
    val cdu: Int = readln().toInt()
    val cint: Int = cdu / 3
    val dint: Int = (cdu - cint * 100) / 10
    val uint: Int = cdu - cint * 100 - dint * 10
    val udc: Int = uint * 100 + dint * 10 + cint
    println(udc)

    println()

    println("Insira um número:")
    var g: Int = readln().toInt()
    when (g) {
        1 -> println("Janeiro")
        2 -> println("Fevereiro")
        3 -> println("Março")
        4 -> println("Abril")
        5 -> println("Maio")
        6 -> println("Junho")
        7 -> println("Julho")
        8 -> println("Agosto")
        9 -> println("Setembro")
        10 -> println("Outubro")
        11 -> println("Novembro")
        12 -> println("Dezembro")
        else -> println("Não é um mês válido.")
    }

    println()

    val teamGoal = mapOf(
        "Benfica" to 5,
        "Sporting" to 9
    )
    for ((k, v) in teamGoal) {
        println("$k = $v golos.")
    }
    if (teamGoal["Benfica"]!! > teamGoal["Sporting"]!!) {
        println("O vencedor é o Benfica.")
    } else if (teamGoal["Benfica"]!! < teamGoal["Sporting"]!!) {
        println("O vencedor é o Sporting.")
    } else {
        println("Empate.")
    }

    println()

    println("Insira um numero maior que 50:")
    val h: Int = readln().toInt()
    var counter: Int = 0
    while (counter != h) {
        if (counter in 50..150) {
            println(counter)
        }
        counter++
    }
}
