Feature: Prueba inicial

    @test1
    Scenario: Filtrar ofertas de empleo por palabra clave
        Given que el usuario está en la tabla de búsqueda de empleo localizada en la url "https://www.alten.es/"
        When ingresa la palabra clave en el campo de búsqueda y presiona Buscar Ofertas
        Then se muestran los resultados de las ofertas relacionadas