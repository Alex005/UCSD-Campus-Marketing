var date = new Date();
var year = date.getFullYear();
var month = date.getMonth();

var search_data = {
  'dept': '',
  'year': '',
  'term': ''
};

$('#search_btn').prop("disabled", "disabled");

$('#dept_valid').hide();
$('#dept_invalid').hide();

$('#dept_text').blur(function() {
  var val = $(this).val().toUpperCase();
  if (Object.keys(depts).includes(val)) {
    $('#dept_valid').show();
    $('#dept_invalid').hide();
    search_data['dept'] = val;
    searchDisable();
  } else {
    $('#dept_invalid').show();
    $('#dept_valid').hide();
  }
});

function searchDisable() {
  console.log(search_data)
  if (search_data['dept'] != '' && search_data['year'] != '' && search_data['term'] != '') {
    $('#search_btn').prop("disabled", "");
  }
}

function setYearSelection() {
  var years = {};
  years[String(year - 2 - 2000)] = String(year - 2) + ' - ' + String(year - 1);
  years[String(year - 1 - 2000)] = String(year - 1) + ' - ' + String(year);

  if (month >= 3) {
    years[String(year - 2000)] = String(year) + ' - ' + String(year + 1);
  }
  $.each(years, function(key, val) {
    $('#year_select').append('<option value="' + key + '">' + val + '</option>');
  });
  $('#year_select').change(function() {
    search_data['year'] = $(this).val();
    searchDisable();
  });
}

function setTermSelection() {
  var quarters = {};
  $('#term_select').change(function() {
    search_data['term'] = $(this).val();
    searchDisable();
  });
}

setYearSelection()
setTermSelection()

depts = {
  'AWP': 'Analytical Writing Program',
  'ANES': 'Anesthesiology',
  'ANTH': 'Anthropology',
  'AUDL': 'Audiology Jt Doc Program',
  'BENG': 'Bioengineering',
  'BIOL': 'Biology',
  'BIOM': 'Biomedical Sciences',
  'CMM': 'Cellular &amp; Molecular Medicine',
  'CHEM': 'Chemistry and Biochemistry',
  'CHIN': 'Chinese Studies Program',
  'CLRE': 'Clincal Research Program',
  'CLPH': 'Clinical Pharmacy',
  'CLIN': 'Clinical Psychology Program',
  'COGS': 'Cognitive Science',
  'COMM': 'Communication',
  'CSE': 'Computer Science &amp; Engineering',
  'ICAM': 'Computing and the Arts',
  'CONT': 'Contemporary Issues Program',
  'CGS': 'Critical Gender Studies Program',
  'CAT': 'Culture, Art &amp; Technology Program',
  'DSC': 'Data Science',
  'DERM': 'Dermatology',
  'DOC': 'Dimensions of Culture Program',
  'ECON': 'Economics',
  'EDS': 'Education Studies',
  'ERC': 'Eleanor Roosevelt College',
  'ECE': 'Electrical &amp; Computer Engineering',
  'EMED': 'Emergency Medicine',
  'ENVR': 'Environmental Studies Program',
  'ESYS': 'Environmental Systems Program',
  'ETHN': 'Ethnic Studies',
  'FMPH': 'Family Medicine &amp; Public Health',
  'FPM': 'Family and Preventive Medicine',
  'FILM': 'Film Studies Program',
  'GMST': 'German Studies Program',
  'GLBH': 'Global Health Program',
  'GPS': 'Global Policy &amp; Strategy',
  'HLAW': 'Health Law Program',
  'HIST': 'History',
  'HDP': 'Human Development Program',
  'HMNR': 'Human Rights',
  'HUM': 'Humanities Program',
  'INTL': 'International Studies Program',
  'JAPN': 'Japanese Studies Program',
  'JUDA': 'Judaic Studies Program',
  'LATI': 'Latin American Studies Program',
  'LHCO': 'Leadership/Health Care Organization',
  'LING': 'Linguistics',
  'LIT': 'Literature',
  'MMW': 'Making of the Modern World',
  'MBC': 'Marine Biodiversity &amp; Conservation',
  'MATS': 'Materials Sci &amp; Engineering Program',
  'MSED': 'Math &amp; Science Educ Jt Doc Program',
  'MATH': 'Mathematics',
  'MAE': 'Mechanical &amp; Aerospace Engineering',
  'MED': 'Medicine',
  'MUIR': 'Muir College',
  'MCWP': 'Muir College Writing Program',
  'MUS': 'Music',
  'NENG': 'NanoEngineering',
  'NEU': 'Neurosciences',
  'OPTH': 'Ophthalmology',
  'ORTH': 'Orthopaedics',
  'PATH': 'Pathology',
  'PEDS': 'Pediatrics',
  'PHAR': 'Pharmacology',
  'PHIL': 'Philosophy',
  'PHYS': 'Physics',
  'POLI': 'Political Science',
  'PSY': 'Psychiatry',
  'PSYC': 'Psychology',
  'RMAS': 'Radiation Medicine and Applied Sci',
  'RAD': 'Radiology',
  'RSM': 'Rady School of Management',
  'RELI': 'Religion, Program for the Study of',
  'RMED': 'Reproductive Medicine',
  'REV': 'Revelle College',
  'SOMI': 'Sch of Med Interdisciplinary Crses',
  'SOE': 'School of Engineering',
  'SOMC': 'School of Medicine',
  'SIO': 'Scripps Institution of Oceanography',
  'SOC': 'Sociology',
  'SE': 'Structural Engineering',
  'SURG': 'Surgery',
  'THEA': 'Theatre and Dance',
  'TWS': 'Third World Studies Program',
  'TMC': 'Thurgood Marshall College',
  'UNAF': 'Unaffiliated',
  'USP': 'Urban Studies &amp; Planning Prog',
  'VIS': 'Visual Arts',
  'WARR': 'Warren College',
  'WCWP': 'Warren College Writing Program',
  'WES': 'Wireless Embedded Systems'
}
