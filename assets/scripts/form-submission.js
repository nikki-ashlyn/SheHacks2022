function logSubmitStepOne(event) {
    alert(`Form Submitted!`);
    event.preventDefault();
  }
  
  var form = document.getElementById('formOne');
  form.addEventListener('submit', logSubmitStepOne);