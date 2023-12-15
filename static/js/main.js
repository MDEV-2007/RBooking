document.addEventListener('DOMContentLoaded', function () {
    const categoryCarousel = document.getElementById('categoryCarousel');
    let isDragging = false;
    let startX;
    let scrollLeft;
  
    categoryCarousel.addEventListener('mousedown', (e) => {
      isDragging = true;
      startX = e.pageX - categoryCarousel.offsetLeft;
      scrollLeft = categoryCarousel.scrollLeft;
    });
  
    categoryCarousel.addEventListener('mouseleave', () => {
      isDragging = false;
    });
  
    categoryCarousel.addEventListener('mouseup', () => {
      isDragging = false;
    });
  
    categoryCarousel.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      e.preventDefault();
      const x = e.pageX - categoryCarousel.offsetLeft;
      const walk = (x - startX) * 3;
      categoryCarousel.scrollLeft = scrollLeft - walk;
    });
  
    categoryCarousel.addEventListener('dragstart', (e) => {
      e.preventDefault();
    });
  
    categoryCarousel.addEventListener('selectstart', (e) => {
      e.preventDefault();
    });
  });
  document.addEventListener('DOMContentLoaded', function () {
    const categoryCarousel = document.getElementById('categoryCarousel');
    let isDragging = false;
    let startX;
    let scrollLeft;
  
    categoryCarousel.addEventListener('mousedown', (e) => {
      isDragging = true;
      startX = e.pageX - categoryCarousel.offsetLeft;
      scrollLeft = categoryCarousel.scrollLeft;
    });
  
    categoryCarousel.addEventListener('mouseleave', () => {
      isDragging = false;
    });
  
    categoryCarousel.addEventListener('mouseup', () => {
      isDragging = false;
    });
  
    categoryCarousel.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      e.preventDefault();
      const x = e.pageX - categoryCarousel.offsetLeft;
      const walk = (x - startX) * 3;
      categoryCarousel.scrollLeft = scrollLeft - walk;
    });
  
    categoryCarousel.addEventListener('dragstart', (e) => {
      e.preventDefault();
    });
  
    categoryCarousel.addEventListener('selectstart', (e) => {
      e.preventDefault();
    });
  });
    