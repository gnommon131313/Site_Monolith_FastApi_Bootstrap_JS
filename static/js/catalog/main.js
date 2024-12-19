import { initializeOnContentLoaded } from './contentLoaded.js';
import { attachButtonEvents } from './btnEventHandlers.js';

document.addEventListener('DOMContentLoaded', function() {
    initializeOnContentLoaded();
    attachButtonEvents();
});