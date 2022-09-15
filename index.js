var firstNameError = document.getElementById("first-name-error");
var lastNameError = document.getElementById("last-name-error");
var phoneError = document.getElementById("phone-error");
var emailError = document.getElementById("email-error");
var pwdError = document.getElementById("pwd-error");
var submitError = document.getElementById("submit-error");

function validateFirstName(){
    var firstName = document.getElementById('first-name').value;

    if(firstName.length == 0){
        firstNameError.innerHTML = 'Name is required';
        return false;
    }
    if(!firstName.match(/^[a-zA-Z]+$/)){
        firstNameError.innerHTML = 'Alphabets only';
        return false;
    }
    firstNameError.innerHTML = 'valid';
    return true;
}

function validateLastName(){
    var lastName = document.getElementById('last-name').value;

    if(lastName.length == 0){
        lastNameError.innerHTML = 'Name is required';
        return false;
    }
    if(!lastName.match(/^[a-zA-Z]+$/)){
        lastNameError.innerHTML = 'Alphabets only';
        return false;
    }
    lastNameError.innerHTML = 'valid';
    return true;
}

function validatePhone(){
    var phone = document.getElementById('phone-number').value;

    if(phone.length == 0){
        phoneError.innerHTML = 'Phone no is required';
        return false;
    }
    if(phone.length !== 10){
        phoneError.innerHTML = 'Phone no should be 10 digits';
        return false;
    }
    if(!phone.match(/^[0-9]{10}$/)){
        phoneError.innerHTML = 'Phone no is required';
        return false;
    }

    phoneError.innerHTML = 'valid';
    return true;
}

function validateEmail(){
    var email = document.getElementById('email').value;

    if(email.length == 0){
        emailError.innerHTML = 'Email is required';
        return false;
    }
    if(!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){
        emailError.innerHTML = 'Email is Invalid';
        return false;
    }

    emailError.innerHTML = 'valid';
    return true;

}

function validatePwd(){
    var password = document.getElementById('pwd').value;

    if(password.length == 0){
        pwdError.innerHTML = 'Password is required';
        return false;
    }
    if(password.length < 6){
        pwdError.innerHTML = 'Password should be more than 5 characters.';
        return false;
    }

    pwdError.innerHTML = 'valid';
    return true;

}

function validateForm(){
    if(!validateFirstName() || !validateLastName() || !validatePhone() || !validateEmail() || !validatePwd()){
        submitError.style.display = 'block';
        submitError.innerHTML = 'Please fix error to submit';
        setTimeout(function(){submitError.style.display = 'none';}, 3000);
        return false;
    }
    alert("the information is stored");
}