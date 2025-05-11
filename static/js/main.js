const form = document.getElementById('assistance-form');
const alertBox = document.getElementById('form-alert');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

document.getElementById("membershipForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const form = e.target;
  const data = Object.fromEntries(new FormData(form).entries());

  const response = await fetch("/submit_membership_request", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    alert("Request submitted successfully!");
    form.reset();
  } else {
    alert("Submission failed. Please try again.");
  }
});

// CSRF token helper (if using Django templates)
function getCookie(name) {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  if (match) return match[2];
}


  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(form);
    const jsonData = Object.fromEntries(formData.entries());

    fetch('/submit-assistance-request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')  // CSRF for Django
      },
      body: JSON.stringify(jsonData)
    })
    .then(res => res.json())
    .then(data => {
      alertBox.classList.remove('d-none', 'alert-danger');
      alertBox.classList.add('alert-success');
      alertBox.textContent = 'Request submitted successfully!';
      form.reset();
    })
    .catch(err => {
      alertBox.classList.remove('d-none', 'alert-success');
      alertBox.classList.add('alert-danger');
      alertBox.textContent = 'There was an error submitting your request.';
    });
  });

  // CSRF helper for Django
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
          cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }