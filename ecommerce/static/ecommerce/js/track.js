// ---- Tracking user clicks ---- //

$(".add-to-cart-btn").click(
function(e) {
    e.preventDefault();
    
    // Get event data
    productId = $(this).data("product");

    if (user != 'AnonymousUser') {
        alert(user + " added product $product to cart".replace("$product", 
        productId));
    } else {
        alert("Please login");
    }
});

$(".view-product-btn").click( 
function(e) {
    e.preventDefault();

    // Get event data
    productId = $(this).data("product");
    
    if (user != 'AnonymousUser') {
        alert(user + " viewed product $product".replace("$product", 
        productId));
    } else {
        alert("Please login");
    }
});