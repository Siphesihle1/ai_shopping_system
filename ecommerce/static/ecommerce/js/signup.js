/* Because i didnt set placeholder values in forms.py they will be set here using vanilla Javascript
//We start indexing at one because CSRF_token is considered and input field 
*/

//Query All input fields
var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder='First Name..';
form_fields[2].placeholder='Last Name..';
form_fields[3].placeholder='Username..';
form_fields[4].placeholder='Email..';
form_fields[5].placeholder='Cellphone Number..';
form_fields[6].placeholder='Enter password...';
form_fields[7].placeholder='Re-enter Password...';


for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}