const cursor = document.querySelector('.cursor');

document.addEventListener('mousemove', e => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
});

document.addEventListener('mousedown', () => cursor.style.transform = 'scale(0.8)');
document.addEventListener('mouseup', () => cursor.style.transform = 'scale(1)');

// Smooth transition saat pindah page
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        document.querySelector('.content').classList.add('fade-out');
    });
});