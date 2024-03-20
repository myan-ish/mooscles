/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
  ],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    fontSize: {
      'xs': '14px',
      'sm': '16px',
      'lg': '21px',
      'xl': '27px',
    },
    fontFamily: {
      'heading': ['Poppins', 'sans-serif'],
      'body': ['Poppins', 'sans-serif'],
    },
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'body': '#F4F7ED',
        'primary': '#16C79A',
        'secondary': '#60ee73',
        'font': '#151a27',
        'white': '#ffffff',
        'black': '#181818',
        'navBgDark': '#23293a',
        'fade': '#2B375260',
        'inputBgDark': '#29334d',
        'inputBgLight': '#e7e9e0',
      },
      transition: {
        'ease-in-out': 'all 0.3s ease-in-out',
      },
      keyframes: {
        'slide-up': {
          '0%': {
            transform: 'translateY(100%)',
          },
          '100%': {
            transform: 'translateY(0)',
          },
        },
        'slide-down': {
          '0%': {
            transform: 'translateY(0)',
          },
          '100%': {
            transform: 'translateY(100%)',
          },
        },
        'fade-in': {
          '0%': {
            opacity: '0',
          },
          '100%': {
            opacity: '1',
          },
        },
      },
      animation: {
        'slide-up': 'slide-up 0.3s ease-in-out',
        'slide-down': 'slide-down 0.3s ease-in-out',
        'fade-in': 'fade-in 0.3s ease-in-out',
      },
    },
  },
  plugins: [],
}
