// ---- Tracking user clicks ---- //

$(".add-to-cart-btn").click(
function(e) {
    e.preventDefault();
    
    // Get event data
    productId = $(this).data("product");

    if (user != 'AnonymousUser') {
        
    }
});

$(".view-product-btn").click( 
function(e) {
    e.preventDefault();

    // Get event data
    productId = $(this).data("product");
    
    if (user != 'AnonymousUser') {
        
    }
});