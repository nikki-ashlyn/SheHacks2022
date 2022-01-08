function logSubmitStepOne(event) {
    var formOne = document.getElementsByClassName("onboarding-form")[0];
    formOne.classList.add("display-none");

    var formTwo = document.getElementsByClassName("onboarding-form-2")[0];
    formTwo.classList.remove("display-none");
    event.preventDefault();
  }

function logSubmitStepTwo(event) {
    alert("DONE");
    event.preventDefault();
  }
  
  var formOne = document.getElementById('formOne');
  formOne.addEventListener('submit', logSubmitStepOne);

  var formTwo = document.getElementById('formTwo');
  formTwo.addEventListener('submit', logSubmitStepTwo);