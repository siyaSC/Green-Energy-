
const phoneNumberInput = document.getElementById('pnumber');
phoneNumberInput.addEventListener('input', () => {
    const phoneNumber = phoneNumberInput.value;
    if (!isValidPhoneNumber(phoneNumber)) {
        phoneNumberInput.setCustomValidity('Please enter a valid phone number');
    } else {
        phoneNumberInput.setCustomValidity('');
    }
});

function isValidPhoneNumber(phoneNumber) {
    const phonePattern = /^(?:\+\d{1,3})?(?:\(\d{3}\))?(?:\d{3}[-]?\d{4})$/;
    return phonePattern.test(phoneNumber);
}

function isValidName(name) {
    const namePattern = /^[A-Za-z-' ]+$/;
    return namePattern.test(name);
}

const firstNameInput = document.getElementById('fname');
const lastNameInput = document.getElementById('lname');

firstNameInput.addEventListener('input', () => {
    const firstName = firstNameInput.value;
    if (!isValidName(firstName)) {
        firstNameInput.setCustomValidity('Please enter a valid first name');
    } else {
        firstNameInput.setCustomValidity('');
    }
});

lastNameInput.addEventListener('input', () => {
    const lastName = lastNameInput.value;
    if (!isValidName(lastName)) {
        lastNameInput.setCustomValidity('Please enter a valid last name');
    } else {
        lastNameInput.setCustomValidity('');
    }
});


const tooltip = document.querySelector('.tooltip');
const elementWithTooltip = document.querySelector('.element-with-tooltip');

elementWithTooltip.addEventListener('mouseenter', () => {
    tooltip.style.display = 'block';
});

elementWithTooltip.addEventListener('mouseleave', () => {
    tooltip.style.display = 'none';
});

const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
    event.preventDefault(); 

    const form = event.target;
    const formData = new FormData(form);

    for (const entry of formData.entries()) {
        console.log(entry[0], entry[1]);
    }
    const confirmationMessage = document.createElement('p');
    confirmationMessage.textContent = 'Form submitted successfully!';
    form.appendChild(confirmationMessage);
});

const contentContainer = document.querySelector('.content-container');

fetch('https://api.example.com/content')
    .then((response) => response.json())
    .then((data) => {
        // Display dynamic content
        contentContainer.innerHTML = data.content;
    })
    .catch((error) => {
        console.error('Error fetching content:', error);
    });

    // Example: Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);

        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});
