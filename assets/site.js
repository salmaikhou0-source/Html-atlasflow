/* Bilingual Support Co. — site behaviour (shared by the English and French pages) */
(function () {
  "use strict";

  /* ================== SETTINGS: fill these in once ==================
     FORM_ENDPOINT: the address of your free Formspree form,
       for example "https://formspree.io/f/abcdwxyz".
     CONTACT_EMAIL: the business email shown on the site,
       for example "bilingualsupportco@gmail.com".
     Leave a setting empty ("") until it exists. */
  var FORM_ENDPOINT = "";
  var CONTACT_EMAIL = "";
  /* ================================================================= */

  var root = document.querySelector("[data-page-lang]");
  var lang = root && root.getAttribute("data-page-lang") === "fr" ? "fr" : "en";

  var text = {
    en: {
      sending: "Sending…",
      sent: "Thanks. We'll reply within one business day.",
      failed: "Your message didn't send. Check your connection and try again.",
      notConnected: "This form isn't connected yet, so your message wasn't sent."
    },
    fr: {
      sending: "Envoi en cours…",
      sent: "Merci. Nous vous répondrons d'ici un jour ouvrable.",
      failed: "Votre message n'a pas été envoyé. Vérifiez votre connexion et réessayez.",
      notConnected: "Ce formulaire n'est pas encore branché : votre message n'a pas été envoyé."
    }
  }[lang];

  /* Business email: shown only once CONTACT_EMAIL is set */
  if (CONTACT_EMAIL) {
    document.querySelectorAll("[data-email]").forEach(function (a) {
      a.textContent = CONTACT_EMAIL;
      a.setAttribute("href", "mailto:" + CONTACT_EMAIL);
    });
    document.querySelectorAll("[data-email-line]").forEach(function (el) {
      el.hidden = false;
    });
  }

  /* Hero ticket: flip the same conversation between French and English */
  document.querySelectorAll("[data-ticket]").forEach(function (ticket) {
    var buttons = ticket.querySelectorAll("[data-show]");
    var panes = ticket.querySelectorAll("[data-pane]");
    var chip = ticket.querySelector("[data-lang-chip]");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var want = btn.getAttribute("data-show");
        buttons.forEach(function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        panes.forEach(function (p) {
          p.hidden = p.getAttribute("data-pane") !== want;
        });
        if (chip) chip.textContent = want === "fr" ? "FR-CA" : "EN-CA";
      });
    });
  });

  /* "Choose this plan" buttons pre-select the plan in the contact form */
  document.querySelectorAll("[data-pick]").forEach(function (link) {
    link.addEventListener("click", function () {
      var input = document.querySelector('input[name="interest"][value="' + link.getAttribute("data-pick") + '"]');
      if (input) input.checked = true;
    });
  });

  /* Contact form */
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    var status = form.querySelector("[data-form-status]");
    var submit = form.querySelector('button[type="submit"]');

    var show = function (msg, kind) {
      status.textContent = msg;
      status.className = "form-status" + (kind ? " " + kind : "");
    };

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!form.reportValidity()) return;

      if (!FORM_ENDPOINT) {
        show(text.notConnected, "err");
        return;
      }

      submit.disabled = true;
      show(text.sending, "");

      var data = new FormData(form);
      data.append("page_language", lang);

      fetch(FORM_ENDPOINT, {
        method: "POST",
        body: data,
        headers: { Accept: "application/json" }
      })
        .then(function (res) {
          if (!res.ok) throw new Error("HTTP " + res.status);
          form.reset();
          show(text.sent, "ok");
        })
        .catch(function () {
          show(text.failed, "err");
        })
        .then(function () {
          submit.disabled = false;
        });
    });
  }

  /* Footer year */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
