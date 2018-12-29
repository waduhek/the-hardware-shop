$(document).ready(function() {
    var quantity = 1;

    $('#increase').click(function(event) {
        quantity += 1;
        str_quantity = '' + quantity;

        $('#quantity').text(str_quantity);
    });

    $('#decrease').click(function(event) {
        quantity = $('#quantity').text();
        quantity = parseInt(quantity);

        if (quantity > 1) {
            quantity -= 1;
            str_quantity = '' + quantity;

            $('#quantity').text(str_quantity);
        }
    });
});