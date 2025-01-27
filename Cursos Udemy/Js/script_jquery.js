$(function(){
    $('#l2').click(function(){
        $('#i2').show();
        $('#i1').hide();
        $('#i3').hide();
        $('#i4').hide();
    });

    
    $('#l1').click(function(){
        $('#i1').show();
        $('#i2').hide();
        $('#i3').hide();
        $('#i4').hide();
    });
    
    $('#l3').click(function(){
        $('#i3').show();
        $('#i1').hide();
        $('#i2').hide();
        $('#i4').hide();
    });
    
    $('#l4').click(function(){
        $('#i4').show();
        $('#i1').hide();
        $('#i3').hide();
        $('#i2').hide();
    });
});