/*$(".delete-from-cart-btn").click(
  function(e) {
    e.preventDefault();
    
    // Get event data
    product_id = $(this).data("product");
    console.log(product_id);

    $.ajax({
      type: 'GET',
      url: "{% url 'deletefromcart' %}",
      data: {"product_id": product_id},
      success: function (response){
        data = response.json();
        alert(data["message"]);      
      },
      error: function(response){
        alert(response["responseJSON"]["error"]);
      }
    }) 
});*/