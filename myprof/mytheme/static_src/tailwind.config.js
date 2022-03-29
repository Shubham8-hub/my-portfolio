/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /* 
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',
        
        /* 
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                // 'violet' : '#fc90ec',
                'blue'   : '#9645ff',
                'sky-blue': '#7765fc',
                'light-violet': '#dd99ff',
                'light-green': '#d8f7a8',
                'light-green-1': '#95e677',
                'red': '#ff0000',
                'light-blue': '#3d4dff',
                'blue-1': '#AB6AF9',
                'border-1': '#4044D3',
                'highlight-1': '#24F0F9',
                'red-1': '#F93324',
                'blue-2': '#00bfff',
                'inner-2': '#005ce6',
                // button color
                'btnn-1': '#73dcff',
                'blue-3': '#14EAFF',
                'aqua-1': '#00ffff7a',
                // about  
                'about-1': '#e6ffe6',
                'about-2': '#99ffbb',
                // resume
                'resume-1': '#f5f7f7',
                'resume-2': '#F9A8C3',
                // project
                'project-1': '#f7f2f7',
                'project-2': '#F8F690',
                // contact
                'contact-1': '#ACF673',
                'contact-2': '#E0F781',
            },
            fontFamily: {
                'head-1': ['Lora', ],
                'head-2': ['Roboto Serif', ],
                // Ui link css ie, Home About me, etc.
                'ui-tabs': ['Fredoka One', ],
                // Homepage font
                // Title : Name font
                'tit': ['Enriqueta', ],
                // Subtitle font
                'sub-tit': ['Josefin Slab', ],
                // About Page Fonts
                // Heading
                'abt-head': ['Chela One', ],
                // Paragraph
                'para-1': ['Source Serif Pro', ],
                'para-3': ['Averia Serif Libre', ],
                'para-4': ['Fredoka', ],
                // About , What do I do title
                'abt-tit': ['Faustina', ],
                'abt-p': ['Karma', ],
                
                // Resume Font
                'abt-p': ['Karma', ],
                
                // Heading fonts ie. Education, Designskill, etc.
                'resume-subhead': ['Ramaraja', ],

                // Education 
                'resume-p-1': ['Domine', ],
                'resume-p-2': ['Amiri', ],
                'resume-p-3': ['Vollkorn', ],
                // design skill block
                'resume-d-1': ['Alegreya', ],
                // Skill font
                'resume-skill': ['League Spartan', ],
                // Skill highlight
                'resume-skill-h': ['Padauk', ],
                // Project title font
                'proj-tit': ['Noticia Text', ],
                // common heading
                'common-heading': ['Concert One', ],
                // contact btn
                'contact-btn': ['Changa', ],
            },
        },
        fontsize: {
            sm: ['30px', '0px'],
        },
        screens: {
            'sm': [{'min': '320px'},
            { 'min': '425px'},],

            'laptop': '1024px',
            'tablet': '768px',
            // => @media (max-wdth: 639px) { ... }

            // '2xl': {'max': '1535px'},
            // // => @media (max-width: 1535px) { ... }
      
            // 'xl': {'max': '1279px'},
            // // => @media (max-width: 1279px) { ... }
      
            // 'lg': {'max': '1023px'},
            // // => @media (max-width: 1023px) { ... }
      
            // 'md': {'max': '767px'},
            // // => @media (max-width: 767px) { ... }
      
          }
        
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
