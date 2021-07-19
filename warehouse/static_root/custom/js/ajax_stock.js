$(document).ready(function() {
    $(document).on('change', '#id_stock_sn', function () {
        let id_item = $('#id_stock_sn :selected').val();
        $.ajax({
            url: '/stock/ajax/getitemcount/',
            method: "GET",
            data: {
                id_item: id_item,
            },
            success: function (res) {
                $('#item_count').text(res.item_cnt);
            },
        });
    });
    $(document).on('click', '#put_btn', function () {
        $('#id_stock_cnt').val($('#item_count').text());
    });
});