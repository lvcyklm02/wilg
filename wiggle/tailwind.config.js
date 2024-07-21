/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./wilg_website/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['"Open Sans"', 'sans-serif'],
      },
      colors: {
        'wilg-purple': '#8150c7',
      },
      fontSize: {
        'h1-global': '4rem',  // Example size for h1, adjust as needed
      },
    },
  },
  plugins: [
    function ({ addBase, theme }) {
      addBase({
        'h1': {
          fontSize: theme('fontSize.h1-global'),
          fontWeight: theme('fontWeight.bold'),
          lineHeight: theme('lineHeight.tight'),
        },
      });
    },
  ],
}

