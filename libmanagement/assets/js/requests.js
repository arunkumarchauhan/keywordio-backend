$("#loginButton").click(function () {
    $.ajax({

        url: 'http://localhost:8000/api/v1/login',

        type: 'POST',

        dataType: 'json',
        data:{
            email:$('#loginEmail').val(),
            password:$('#loginPassword').val()
        },
        success: function (data, textStatus, xhr) {
            console.log(data);

            $('#loginMessage').append( "<p>"+data.message+"</p>" );

        },

        error: function (xhr, textStatus, errorThrown) {
            console.log(xhr)

            console.log(textStatus);

        }

    });

});

$("#registerButton").click(function () {
    $.ajax({

        url: 'http://localhost:8000/api/v1/register',

        type: 'POST',

        dataType: 'json',
        data:{
            email:$('#registerEmail').val(),
            name:$('#registerName').val(),
            password:$('#registePassword').val(),
        },
        success: function (data, textStatus, xhr) {
            console.log(data);
            $('#registerMessage').append( "<p>"+data.message+"</p>" );

        },

        error: function (xhr, textStatus, errorThrown) {
            console.log(xhr)

            console.log(textStatus);

        }

    });

});