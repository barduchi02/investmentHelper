$(document).ready( function () {
    $('#tunnels_table').DataTable({
        "columnDefs":[
            { targets: [8, 9, 10], orderable: false }
        ],
        "language": {
            "decimal": ",",
            "emptyTable":     "não há dados disponíveis",
            "info":           "Mostrando _START_ a _END_ de _TOTAL_ túneis",
            "infoEmpty":      "Mostrando 0 a 0 de 0 túneis",
            "infoFiltered": "(filtrado de _MAX_ registros no total)",
            "thousands":      ".",
            "lengthMenu": "Mostrando _MENU_ registros por página",
            "loadingRecords": "Carregando...",
            "search":         "Buscar:",
            "zeroRecords": "Nenhum túnel encontrado",
            "paginate": {
                "first":      "Primeiro",
                "last":       "Último",
                "next":       "Próximo",
                "previous":   "Anterior"
            },
            "aria": {
                "sortAscending":  ": clique para ordenar de forma crescente",
                "sortDescending": ": clique para ordenar de forma decrescente"
            }
        }
    });
} );