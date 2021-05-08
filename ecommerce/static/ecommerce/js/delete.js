$(".delete-from-cart-btn").click(
 function(e) {
     e.preventDefault();
     
     // Get event data
     product_id = $(this).data("product");
 
    $.ajax({
     type: 'GET',
     url: "{% url 'deletefromcart' %}",
     data: {"product_id": product_id},
     success: function (response){
       alert("Item deleted.")      
     },
     error: function(response){
      alert(response["responseJSON"]["error"]);
     }
    }) 
 });