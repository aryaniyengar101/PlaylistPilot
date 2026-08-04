/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#0D1117",
        surface: "#161B22",
        border: "#30363D",
        primary: "#F0F6FC",
        secondary: "#8B949E",
        accent: "#1DB954",
        accentHover: "#1ED760",
        danger: "#F85149",
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
        heading: ["Sora", "sans-serif"],
      },
    },
  },
  plugins: [],
}