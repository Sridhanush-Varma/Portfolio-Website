// Add smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add animation to skill items
window.addEventListener('load', () => {
    const skillItems = document.querySelectorAll('.skill-item');
    skillItems.forEach((item, index) => {
        item.style.animation = `fadeIn 0.5s ease ${index * 0.1}s forwards`;
    });
});

// Add hover effect to experience items
const experienceItems = document.querySelectorAll('.experience-item');
experienceItems.forEach(item => {
    item.addEventListener('mouseenter', () => {
        item.style.transform = 'scale(1.02)';
        item.style.transition = 'transform 0.3s ease';
    });
    
    item.addEventListener('mouseleave', () => {
        item.style.transform = 'scale(1)';
    });
});

// Show initial section
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('summary').classList.add('active');
});

// Tab switching functionality
const tabs = document.querySelectorAll('.tab');
const sections = document.querySelectorAll('.section');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove active class from all tabs and sections
        tabs.forEach(t => t.classList.remove('active'));
        sections.forEach(section => section.classList.remove('active'));

        // Add active class to clicked tab and corresponding section
        tab.classList.add('active');
        const sectionId = tab.getAttribute('data-tab');
        document.getElementById(sectionId).classList.add('active');
    });
});

// Admin authentication state
let isAdmin = false;
const ADMIN_PASSWORD = "Deepika@04"; // In production, this should be handled securely

// Profile picture update functionality with admin check
document.addEventListener('DOMContentLoaded', () => {
    const profileUpload = document.getElementById('profile-upload');
    const profilePicture = document.getElementById('profile-picture');
    const uploadButton = document.querySelector('.upload-button');

    // Hide upload button by default
    uploadButton.style.display = 'none';

    // Check if admin is logged in
    const adminLoginButton = document.createElement('button');
    adminLoginButton.textContent = 'Admin Login';
    adminLoginButton.className = 'admin-login-btn';
    document.querySelector('.profile-section').appendChild(adminLoginButton);

    adminLoginButton.addEventListener('click', () => {
        const password = prompt("Enter admin password:");
        if (password === ADMIN_PASSWORD) {
            isAdmin = true;
            checkUpdateEligibility();
            adminLoginButton.style.display = 'none';
        } else {
            alert("Invalid password!");
        }
    });

    function checkUpdateEligibility() {
        const lastUpdateDate = localStorage.getItem('lastProfileUpdateDate');
        const currentDate = new Date().toISOString().split('T')[0];
        
        if (!lastUpdateDate || isEligibleForUpdate(lastUpdateDate)) {
            uploadButton.style.display = 'block';
        } else {
            const nextUpdateDate = new Date(lastUpdateDate);
            nextUpdateDate.setFullYear(nextUpdateDate.getFullYear() + 1);
            alert(`Profile picture can only be updated after ${nextUpdateDate.toDateString()}`);
        }
    }

    function isEligibleForUpdate(lastUpdateDate) {
        const lastUpdate = new Date(lastUpdateDate);
        const currentDate = new Date();
        const yearDifference = currentDate.getFullYear() - lastUpdate.getFullYear();
        
        return yearDifference >= 1;
    }

    profileUpload.addEventListener('change', (e) => {
        if (!isAdmin) {
            alert("Only admin can update the profile picture!");
            return;
        }

        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                profilePicture.src = e.target.result;
                localStorage.setItem('profilePicture', e.target.result);
                localStorage.setItem('lastProfileUpdateDate', new Date().toISOString().split('T')[0]);
                uploadButton.style.display = 'none';
            };
            reader.readAsDataURL(file);
        }
    });

    // Load saved profile picture
    const savedProfilePicture = localStorage.getItem('profilePicture');
    if (savedProfilePicture) {
        profilePicture.src = savedProfilePicture;
    }
});