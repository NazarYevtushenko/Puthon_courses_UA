прочитать 
Глава № 32 Основы исключений. 918-927 Lutz. 20 баллов

Скинуть файлик с примерами всех конструкций КРОМЕ менеджера контекста. With/as. 20 баллов

Задача 20 баллов написать функцию которая принимает от пользователя 2 аргумента и делит оlин на другой.

при попытке деления на ноль вывести пользователю "ай яй яй делить на ноль можно не многим"

Все остальные исключения с поймать и вывести их значение в текстовом формате.

И в любом случае вывести. " I 'am happy that you learn python"

пройти тест 20 баллов https://holypython.com/advanced-python-exercises/exercise-3-try-except/

там есть второе задание с pass. С этого смеются! так делать нельзя!. Но для теста можно)))

20 баллов Попробовать понять. Патерн Итератор https://refactoring.guru/ru/design-patterns/iterator/python/example

Задача повышенной Интересности. Попробовать посмотреть на написанный код и сделать его более надежным. Любые изменения приветствуются.

просмотреть каждую программу и посмотреть как она может упасть. Попробовать ее зафейлить.

Во время тестирования заметить какие ошибки появляется

используя исключения изменить код. И не только исключения, а и фантазию.

def example1():
    for i in range( 3 ):
        x = int( input( "enter a number: " ) )
        y = int( input( "enter another number: " ) )
        print( x, '/', y, '=', x/y )

def example2( L ):
    print( "\n\nExample 2" )
    sum = 0
    sumOfPairs = []
    for i in range( len( L ) ):
        sumOfPairs.append( L[i]+L[i+1] )

    print( "sumOfPairs = ", sumOfPairs )


def printUpperFile( fileName ):
   file = open( fileName, "r" )
   for line in file:
       print( line.upper() )
   file.close()
    
def main():
    example1()
    L = [ 10, 3, 5, 6, 9, 3 ]
    example2( L )
    example2( [ 10, 3, 5, 6, "NA", 3 ] )
    example3( [ 10, 3, 5, 6 ] )

    printUpperFile( "doesNotExistYest.txt" )
    printUpperFile( "./Dessssktop/misspelled.txt" )

main()
Работу с файлами мы не проходи. Тему освещать будем но можно и самому глянуть про функцию open() что она делает да как.