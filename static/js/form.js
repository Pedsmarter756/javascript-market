$(document).ready(function () {
    $('.sidenav').sidenav();
    // Show validation message on material select dropdown
    $('select').formSelect();
    $("select[required]").css({
        position: "absolute",
        display: "inline",
        height: 0,
        padding: 0,
        width: 0,
    });

    // Button
    $("#add-technic-btn").click(function () {
        $("#form-field:last").append(getHtml());
    });

    function getHtml() {
        return '<div class="input-field">\
    <input type="text" class="validate" id="technic" name="technic" required />\
    <label for="technic">technic (e.g:Diesel,4x4,....)</label>\
    </div>';
    }

    // Remove  Button
    $("#remove-technic-btn").click(function () {
        $("#form-field").children("div:last").remove()
    })


});