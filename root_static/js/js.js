$(document).ready(function () {
    /*open modal*/
    $('#inputClick').focus(function () {
        $('#add').modal('show');
    })

    /* change bakground for add modal*/
    $('#formAddNote input[name=colors]').focus(function () {
        $('#add .modal-content').css('background', $(this).val())
    })

    $('#editForm input[name=colors]+label').click(function () {
        $('#edit .modal-content').css('background', $('#' + $(this).attr('for')).val())
    })

    $('.side').width($('.sideAccount').width())
    $('[name="avatar"]').change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (ev) {
                $('#show-up').attr('src', ev.target.result);
            }
            reader.readAsDataURL(this.files[0])
        }
    });
    $('.sideAccount img').click(function () {
        $('#up-img').modal('show')
    });
});

function msg(text) {
    $.toast.show({
        text: text,
        align: 'top',
        animate: 'slide',
        closeBtn: 'true'
    })
}