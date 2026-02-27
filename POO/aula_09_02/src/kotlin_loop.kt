fun main() {
    for (i in 1..200) {
        var ilast: Int = i - 1
        var itotal: Int = i + ilast
        println(itotal)
    }

    println()

    for (i in 10 downTo 1) {
        var ilast: Int = i - 1
        var itotal: Int = i + ilast
        println(itotal)
    }

    println()

    val a = arrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for (i in 0 until a.size) {
        println(a[i])
    }

    println()

    var i: Int = 0
    while (i <= 10) {
        println(i)
        i++
    }
}