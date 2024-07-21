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
        'h1-global': '4rem',
        'h2-global': '2rem',
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
          marginTop: theme('margin.4'),
          marginBottom: theme('margin.4'),
        },
        'h2': {
          fontSize: theme('fontSize.h2-global'),
          fontWeight: theme('fontWeight.bold'),
          lineHeight: theme('lineHeight.tight'),
          marginTop: theme('margin.4'),
          marginBottom: theme('margin.4'),
        },
        'h3': {
          fontWeight: theme('fontWeight.bold'),
          lineHeight: theme('lineHeight.tight'),
          marginTop: theme('margin.4'),
          marginBottom: theme('margin.4'),
        },
        'p': {
          marginTop: theme('margin.4'),
          marginBottom: theme('margin.4'),
        },
        'a:hover': {
          textDecoration: 'underline',
          color: theme('colors.wilg-purple'),
        },
      });
    },
  ],
}

