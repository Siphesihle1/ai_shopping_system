// ---- Tracking user clicks ---- //

var url = '/store_customer_activity/';

/*$.ajaxSetup({
    headers: {
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken
    }
});*/

var headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken
};

$(".add-to-cart-btn").click(
function(e) {
    e.preventDefault();
    
    // Get event data
    productId = $(this).data("product");

    if (user != 'AnonymousUser') {
        
        // Send an async request with the data to the backend
        
        fetch(url, {
            method: 'POST',
            headers: headers,          
            body: JSON.stringify({'product_id': productId, 'action': 'add'})
        })
        .then((response) => {
            // Convert to JSON
            return response.json();
        })
        .then((data) => {
            // Output the response
            console.log(data["message"]);
        })
        .catch((error) => {
            console.log("Request failed", error);
        });
    }
});


$(".view-product-btn").click( 
function(e) {
    e.preventDefault();

    // Get event data
    productId = $(this).data("product");
    
    if (user != 'AnonymousUser') {
        // Send async request with the data to the backend
        
        fetch(url, {
            method: 'POST',
            headers: headers,          
            body: JSON.stringify({'product_id': productId, 'action': 'view'})
        })
        .then((response) => {
            // Convert to JSON
            return response.json();
        })
        .then((data) => {
            // Output the response
            console.log(data["message"]);
        })
        .catch((error) => {
            console.log("Request failed", error);
        });
    }
});
    