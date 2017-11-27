$(document).ready(function() {

    $(document).on('click', '#btnPredict', function(e) {
        if ($("#elevation").val() === "") return;
        if ($("#wind").val() === "") return;
        if ($("#precipitation").val() === "") return;
        if ($("#maxTemprature").val() === "") return;

        $.ajax({
            type: 'POST',
            url: $("#btnPredict").data("url"),
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                    "latitude": $("#latitude").val(),
                    "longitude": $("#longitude").val(),
                    "elevation": $("#elevation").val(),
                    "wind": $("#wind").val(),
                    "precipitation": $("#precipitation").val(),
                    "maxTemprature": $("#maxTemprature").val()
                }, null, '\t'),
            dataType: "json",
            beforeSend: function(xhr) {
                $("#predictionResult").hide();
            },
            success: function(data, textStatus, xhr) {
                if (xhr.status === 200) {
                    $("#dt_result").html(data.dt_result);
                    $("#ann_result").html(data.ann_result);
                    $("#rf_result").html(data.rf_result);
                }
            },
            complete: function(xhr, textStatus) {
                if (xhr.status === 200) {
                    $("#predictionResult").show(500);
                }
            }
        });
    });
});