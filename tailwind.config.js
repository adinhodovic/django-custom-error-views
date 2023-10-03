/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./django_custom_error_views/**/*.{html,js}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'Roboto'],
      },
    },
  },
  plugins: [],
};
