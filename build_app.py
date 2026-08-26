
# This script generates the index.html for the RMC Sales & Staff System

html_parts = []

html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>RMC Sales &amp; Staff System</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js"></script>
  <style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--p:#1a56db;--a:#f59e0b;--d:#e02424;--s:#057a55;--pu:#7c3aed;--bg:#f4f6fb;--card:#fff;--b:#e2e8f0;--t:#1e293b;--m:#64748b;--r:10px;--sh:0 2px 16px rgba(30,41,59,.10)}
body{font-family:'Segoe UI',Arial,sans-serif;background:var(--bg);color:var(--t);min-height:100vh}
header{background:linear-gradient(135deg,#1a56db,#1245b0);color:#fff;padding:0 18px;display:flex;align-items:center;justify-content:space-between;min-height:62px;box-shadow:0 2px 12px rgba(26,86,219,.25);position:sticky;top:0;z-index:100;flex-wrap:wrap;gap:6px}
.hl{display:flex;align-items:center;gap:10px}
.hl .ico{font-size:26px}
.ht h1{font-size:1.07rem;font-weight:700}
.ht p{font-size:.7rem;opacity:.8}
.ha{display:flex;gap:6px;flex-wrap:wrap;padding:7px 0}
.btn{display:inline-flex;align-items:center;gap:5px;padding:7px 13px;border-radius:7px;border:none;cursor:pointer;font-size:.82rem;font-weight:600;transition:all .18s;white-space:nowrap}
.bw{background:#fff;color:var(--p)}.bw:hover{background:#e8f0fe}
.ba{background:var(--a);color:#fff}.ba:hover{background:#d97706}
.bs{background:var(--s);color:#fff}.bs:hover{background:#065f46}
.bd{background:var(--d);color:#fff}.bd:hover{background:#9b1c1c}
.bp{background:var(--pu);color:#fff}.bp:hover{background:#6d28d9}
.bo{background:transparent;color:var(--p);border:1.5px solid var(--p)}.bo:hover{background:#e8f0fe}
.bsm{padding:5px 9px;font-size:.77rem}
main{max-width:1440px;margin:0 auto;padding:18px 13px}
.sg{display:grid;grid-template-columns:repeat(auto-fit,minmax(145px,1fr));gap:11px;margin-bottom:16px}
.sc{background:var(--card);border-radius:var(--r);padding:14px;box-shadow:var(--sh);border-left:4px solid var(--p)}
.sc.a{border-left-color:var(--a)}.sc.s{border-left-color:var(--s)}.sc.d{border-left-color:var(--d)}.sc.pu{border-left-color:var(--pu)}
.sl{font-size:.72rem;color:var(--m);font-weight:700;text-transform:uppercase;letter-spacing:.4px;margin-bottom:3px}
.sv{font-size:1.65rem;font-weight:800}
.tabs{display:flex;border-bottom:2px solid var(--b);margin-bottom:14px;overflow-x:auto}
.tb{padding:9px 18px;border:none;background:transparent;font-size:.85rem;font-weight:600;color:var(--m);cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-2px;transition:all .15s;white-space:nowrap}
.tb.act{color:var(--p);border-bottom-color:var(--p)}
.tb:hover{background:#f1f5f9}
.tp{display:none}.tp.act{display:block}
.toolbar{background:var(--card);border-radius:var(--r);padding:13px;box-shadow:var(--sh);margin-bottom:13px;display:flex;flex-wrap:wrap;gap:9px;align-items:center}
.sw{flex:1;min-width:170px;position:relative}
.sw input{width:100%;padding:8px 11px 8px 34px;border:1.5px solid var(--b);border-radius:7px;font-size:.875rem;outline:none}
.sw input:focus{border-color:var(--p)}
.sw .si{position:absolute;left:9px;top:50%;transform:translateY(-50%)}
select.fs{padding:8px 9px;border:1.5px solid var(--b);border-radius:7px;font-size:.81rem;background:#fff;outline:none;cursor:pointer}
select.fs:focus{border-color:var(--p)}
.tc{background:var(--card);border-radius:var(--r);box-shadow:var(--sh);overflow:hidden;margin-bottom:18px}
.tch{padding:13px 16px;border-bottom:1px solid var(--b);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:7px}
.tch h2{font-size:.93rem;font-weight:700}
.tr2{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:.8rem}
thead th{background:#f1f5f9;color:var(--m);font-weight:700;text-transform:uppercase;letter-spacing:.3px;padding:9px 11px;text-align:left;border-bottom:2px solid var(--b);white-space:nowrap;cursor:pointer;user-select:none}
thead th:hover{background:#e2e8f0}
tbody tr:hover{background:#f8fafc}
tbody tr:nth-child(even){background:#fafbfd}
tbody tr:nth-child(even):hover{background:#f1f5f9}
td{padding:8px 11px;border-bottom:1px solid #f1f5f9;vertical-align:top}
.nd{text-align:center;padding:35px;color:var(--m)}
.badge{display:inline-block;padding:2px 8px;border-radius:20px;font-size:.7rem;font-weight:700}
.bb{background:#dbeafe;color:#1e40af}.bg{background:#d1fae5;color:#065f46}.by{background:#fef3c7;color:#92400e}
.br{background:#fee2e2;color:#991b1b}.bgy{background:#f1f5f9;color:#475569}
.bpu{background:#ede9fe;color:#5b21b6}.bor{background:#ffedd5;color:#9a3412}
.ra{display:flex;gap:4px}
.ib{border:none;background:transparent;cursor:pointer;padding:4px 5px;border-radius:5px;font-size:14px}
.ib:hover{background:#f1f5f9}
.pag{display:flex;align-items:center;justify-content:space-between;padding:11px 16px;border-top:1px solid var(--b);flex-wrap:wrap;gap:7px}
.pi{font-size:.8rem;color:var(--m)}
.pbs{display:flex;gap:3px}
.pb{padding:5px 9px;border:1.5px solid var(--b);background:#fff;border-radius:5px;cursor:pointer;font-size:.8rem}
.pb:hover,.pb.act{background:var(--p);color:#fff;border-color:var(--p)}
.pb:disabled{opacity:.35;cursor:not-allowed}
.mo{position:fixed;inset:0;background:rgba(15,23,42,.45);z-index:200;display:flex;align-items:center;justify-content:center;padding:12px;opacity:0;pointer-events:none;transition:opacity .2s}
.mo.open{opacity:1;pointer-events:all}
.md{background:#fff;border-radius:14px;width:100%;max-width:660px;max-height:92vh;overflow-y:auto;box-shadow:0 8px 40px rgba(15,23,42,.22);transform:scale(.95);transition:transform .2s}
.mo.open .md{transform:scale(1)}
.mh{padding:17px 21px;border-bottom:1px solid var(--b);display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;background:#fff;z-index:1}
.mh h3{font-size:1rem;font-weight:700}
.mcl{border:none;background:transparent;font-size:19px;cursor:pointer;color:var(--m);padding:4px 6px;border-radius:5px}
.mcl:hover{background:#f1f5f9}
.mb2{padding:20px}
.mf2{padding:13px 20px;border-top:1px solid var(--b);display:flex;justify-content:flex-end;gap:8px}
.fg{display:grid;grid-template-columns:1fr 1fr;gap:13px}
.fi{display:flex;flex-direction:column;gap:4px}
.fi.full{grid-column:1/-1}
.fi label{font-size:.74rem;font-weight:700;color:var(--m);text-transform:uppercase}
.fi input,.fi select,.fi textarea{padding:8px 10px;border:1.5px solid var(--b);border-radius:7px;font-size:.875rem;outline:none;font-family:inherit}
.fi input:focus,.fi select:focus,.fi textarea:focus{border-color:var(--p)}
.fi textarea{resize:vertical;min-height:60px}
.sgr2{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:13px;padding:16px}
.scard{background:#f8fafc;border:1.5px solid var(--b);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:8px;position:relative;transition:box-shadow .15s}
.scard:hover{box-shadow:0 4px 18px rgba(26,86,219,.10);border-color:#c7d7f8}
.sav{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;font-weight:700;color:#fff;flex-shrink:0}
.stop{display:flex;align-items:center;gap:9px}
.snm{font-weight:700;font-size:.93rem}
.srl{font-size:.74rem;color:var(--m)}
.sdt{font-size:.79rem;color:var(--m);display:flex;align-items:center;gap:5px}
.sca{position:absolute;top:9px;right:9px;display:flex;gap:3px}
.tc2{position:fixed;bottom:18px;right:18px;z-index:999;display:flex;flex-direction:column;gap:5px}
.toast{background:var(--t);color:#fff;padding:10px 15px;border-radius:8px;font-size:.83rem;font-weight:500;box-shadow:0 4px 16px rgba(0,0,0,.2);animation:sIn .22s ease}
.toast.success{background:var(--s)}.toast.error{background:var(--d)}
@keyframes sIn{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}
.dg{display:grid;grid-template-columns:1fr 1fr;gap:11px}
.di label{font-size:.72rem;font-weight:700;color:var(--m);text-transform:uppercase;display:block;margin-bottom:2px}
.di .val{font-size:.88rem}
.di.full{grid-column:1/-1}
.ph{display:none;text-align:center;margin-bottom:11px}
@media print{header,.toolbar,.sg,.tch .btn,.ra,.pag,.mo,.tc2,.tabs{display:none!important}body{background:#fff}main{padding:0;max-width:100%}.tc{box-shadow:none;border:1px solid #ccc}.ph{display:block!important}table{font-size:8.5pt}thead th,tbody tr:nth-child(even){-webkit-print-color-adjust:exact;print-color-adjust:exact}.tp{display:block!important}#tp-2,#tp-3,#tp-4,#tp-5{display:none!important}}
@media(max-width:640px){header{min-height:auto;padding:10px}.fg{grid-template-columns:1fr}.sg{grid-template-columns:repeat(2,1fr)}.dg{grid-template-columns:1fr}}
  </style>
</head>
<body>
<header>
  <div class="hl">
    <span class="ico">&#127959;</span>
    <div class="ht"><h1>RMC Sales &amp; Staff System</h1><p>Ready-Mix Concrete &mdash; Sales Management</p></div>
  </div>
  <div class="ha">
    <button class="btn bw" onclick="openAddVisitModal()">&#10133; Add Visit</button>
    <button class="btn bp" onclick="openAddStaffModal()">&#128100; Add New Staff</button>
    <button class="btn ba" onclick="exportPDF()">&#128196; PDF Report</button>
    <button class="btn bw" onclick="window.print()">&#128424; Print</button>
  </div>
</header>
<div class="tc2" id="tc2"></div>
<div class="mo" id="mo" onclick="hoc(event)">
  <div class="md">
    <div class="mh"><h3 id="mt">Modal</h3><button class="mcl" onclick="closeModal()">&#x2715;</button></div>
    <div class="mb2" id="mb2"></div>
    <div class="mf2" id="mf2"></div>
  </div>
</div>
<main>
  <div class="sg" id="sg"></div>
  <div class="tabs">
    <button class="tb act" onclick="swTab(this,'tp-1')">&#128203; All Visits</button>
    <button class="tb" onclick="swTab(this,'tp-2')">&#9200; Upcoming</button>
    <button class="tb" onclick="swTab(this,'tp-3')">&#128101; Staff</button>
    <button class="tb" onclick="swTab(this,'tp-4')">&#127970; Office Staff Work</button>
    <button class="tb" onclick="swTab(this,'tp-5')">&#128202; Analytics</button>
  </div>
  <div class="tp act" id="tp-1">
    <div class="toolbar">
      <div class="sw"><span class="si">&#128269;</span><input type="text" id="srch" placeholder="Search site, customer, contractor, grade..." oninput="applyF()"></div>
      <select class="fs" id="fsp" onchange="applyF()"><option value="">All Salespersons</option></select>
      <select class="fs" id="fgr" onchange="applyF()"><option value="">All Grades</option></select>
      <select class="fs" id="fdt" onchange="applyF()"><option value="">All Dates</option></select>
      <button class="btn bo bsm" onclick="clrF()">&#x2715; Clear</button>
    </div>
    <div class="tc">
      <div class="ph"><h2>RMC Sales Visit Report</h2><p id="pd"></p></div>
      <div class="tch">
        <h2>Visit Records</h2>
        <div style="display:flex;gap:7px;align-items:center;flex-wrap:wrap">
          <button class="btn bs bsm" onclick="expCSV()">&#11015; CSV</button>
          <span id="rc" style="font-size:.81rem;color:var(--m)"></span>
        </div>
      </div>
      <div class="tr2"><table><thead><tr>
        <th>#</th>
        <th onclick="srt('sp')">Salesperson &#8597;</th>
        <th onclick="srt('vd')">Visit Date &#8597;</th>
        <th>Customer</th><th>Contact</th><th>Contractor</th><th>Cont.No.</th>
        <th onclick="srt('si')">Site/Project &#8597;</th>
        <th>Address</th>
        <th onclick="srt('ar')">Area &#8597;</th>
        <th onclick="srt('gr')">Grade &#8597;</th>
        <th onclick="srt('rd')">Req.Date &#8597;</th>
        <th>Remarks</th><th>Actions</th>
      </tr></thead><tbody id="tb"></tbody></table></div>
      <div class="pag" id="pgb"></div>
    </div>
  </div>
  <div class="tp" id="tp-2">
    <div class="tc"><div class="tch"><h2>&#9200; Upcoming Requirements (Next 30 Days)</h2></div>
      <div class="tr2"><table><thead><tr>
        <th>Salesperson</th><th>Customer</th><th>Contractor</th><th>Site</th>
        <th>Area</th><th>Grade</th><th>Required Date</th><th>Days Left</th><th>Remarks</th>
      </tr></thead><tbody id="utb"></tbody></table></div></div>
  </div>
  <div class="tp" id="tp-3">
    <div class="tc">
      <div class="tch"><h2>&#128101; Staff Directory</h2><button class="btn bp" onclick="openAddStaffModal()">&#128100; Add New Staff</button></div>
      <div id="stgr" class="sgr2"></div>
    </div>
  </div>
  <div class="tp" id="tp-4">
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:13px">
      <div class="tc" style="flex:1;min-width:250px">
        <div class="tch"><h2>&#127970; Office Staff</h2><button class="btn bp" onclick="openAddOSModal()">&#128100; Add Staff</button></div>
        <div id="osl" style="padding:13px;display:flex;flex-direction:column;gap:8px"></div>
      </div>
      <div class="tc" style="flex:2;min-width:310px">
        <div class="tch"><h2>&#128221; Work Log</h2><button class="btn bs bsm" onclick="openAddWLModal()">&#10133; Add Work Entry</button></div>
        <div class="tr2"><table><thead><tr>
          <th>#</th><th>Staff</th><th>Date</th><th>Task / Work Done</th>
          <th>Status</th><th>Priority</th><th>Notes</th><th>Actions</th>
        </tr></thead><tbody id="wlb"></tbody></table></div>
      </div>
    </div>
  </div>
  <div class="tp" id="tp-5">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:15px">
      <div class="tc"><div class="tch"><h2>&#128202; Visits by Salesperson</h2></div>
        <table><thead><tr><th>Salesperson</th><th>Visits</th><th>Total Area</th></tr></thead><tbody id="an1"></tbody></table></div>
      <div class="tc"><div class="tch"><h2>&#129521; Concrete Grade Mix</h2></div>
        <table><thead><tr><th>Grade</th><th>Count</th><th>%</th></tr></thead><tbody id="an2"></tbody></table></div>
      <div class="tc"><div class="tch"><h2>&#128101; Staff by Department</h2></div>
        <table><thead><tr><th>Department</th><th>Count</th></tr></thead><tbody id="an3"></tbody></table></div>
    </div>
  </div>
</main>
""")

html_parts.append("""<script>
// ===== DATA =====
var R=[
{id:1,sp:"Parvinder Kumar",vd:"2026-08-22",cu:"NIKHIL & PARDEEP",cn:"NA",co:"PARDEEP",cc:"9555445836",si:"RELEMAC TECHNOLOGIES PVT LTD",sa:"MALHA MAJRA",ar:"",gr:"",rd:"",rm:"MADAN MUNSI 8938045177"},
{id:2,sp:"Parvinder Kumar",vd:"2026-08-22",cu:"RINKU AGGARWAR",cn:"9999747552",co:"PARDEEP",cc:"9555445836",si:"MALHA MAJRA",sa:"MALHA MAJRA",ar:"1000",gr:"M25",rd:"2026-09-06",rm:"MADAN MUNSI 8938045177"},
{id:3,sp:"Parvinder Kumar",vd:"2026-08-22",cu:"ARYAN DAHIYA",cn:"9868349897",co:"ARYAN DAHIYA",cc:"9868349897",si:"MALHA MAJRA",sa:"MALHA MAJRA",ar:"2000",gr:"M25",rd:"2026-08-29",rm:"ONLY FLOORING"},
{id:4,sp:"Parvinder Kumar",vd:"2026-08-22",cu:"ANIL GUPTA",cn:"",co:"RAJAN",cc:"7879858395",si:"MALHA MAJRA",sa:"MALHA MAJRA",ar:"1700",gr:"M25",rd:"2026-08-29",rm:"RINKU 9992800401"},
{id:5,sp:"Parvinder Kumar",vd:"2026-08-22",cu:"ANIL GUPTA",cn:"",co:"RAJAN",cc:"7879858395",si:"MALHA MAJRA",sa:"MALHA MAJRA",ar:"11000",gr:"M25",rd:"",rm:"FLORING & LANTER"},
{id:6,sp:"Parvinder Kumar",vd:"2026-08-22",cu:"RAJ KUMAR",cn:"9818169834",co:"KAPIL",cc:"9973066337",si:"MALHA MAJRA",sa:"MALHA MAJRA",ar:"10000",gr:"M25",rd:"2026-09-11",rm:"NEAR RADHA SWAMI SATSANG NAHRI ROAD"},
{id:7,sp:"Pawan Kumar",vd:"2026-08-21",cu:"NA",cn:"NA",co:"Chandan",cc:"7979802368",si:"Plot no. 27-28",sa:"Sec-7 Rajdhani",ar:"",gr:"",rd:"",rm:""},
{id:8,sp:"Pawan Kumar",vd:"2026-08-21",cu:"NA",cn:"NA",co:"SONU",cc:"9991417151",si:"SHOWROOM",sa:"LABOU CHOWK KHARKHODA",ar:"1000",gr:"",rd:"",rm:""},
{id:9,sp:"Pawan Kumar",vd:"2026-08-21",cu:"NA",cn:"NA",co:"ANKUR",cc:"8640000709",si:"SANT KABIR FARM HOUSE",sa:"DELHI ROAD KHARKHODA",ar:"",gr:"",rd:"",rm:"OLD RMC DEALER DHOLPUR RMC PLANT"},
{id:10,sp:"Pawan Kumar",vd:"2026-08-22",cu:"NA",cn:"NA",co:"NITIN GUPTA",cc:"9871066092",si:"PLOT NO. 2500",sa:"IMT KHARKHODA",ar:"800",gr:"",rd:"",rm:"WHEN REQURED CALL"},
{id:11,sp:"Pawan Kumar",vd:"2026-08-22",cu:"NA",cn:"NA",co:"J K DUBEY",cc:"9971769836",si:"PLOT NO. 2503",sa:"IMT KHARKHODA",ar:"800",gr:"M25",rd:"2026-08-28",rm:"LABOUR THEKEDAR TILAK RAJ 7289940157"},
{id:12,sp:"Pawan Kumar",vd:"2026-08-22",cu:"NA",cn:"NA",co:"BIMAL PARSHAD",cc:"7633894798",si:"POWAR HOUSE",sa:"IMT KHARKHODA",ar:"",gr:"M40",rd:"2026-09-02",rm:"SUPERVISOR DHANJAY 9570255627 (QUOTATION GIVEN WITH GST 6077/-)"},
{id:13,sp:"Pawan Kumar",vd:"2026-08-23",cu:"RAMBIR RATHI",cn:"9811960900",co:"YOGESH",cc:"8930348669",si:"PLOT NO. 344",sa:"IMT KHARKHODA",ar:"25000",gr:"M10/M30",rd:"2026-09-23",rm:"PCC AND RCC BOTH REQUIRED LAST RCC SUPPLIER LADRAWAN PLANT"},
{id:14,sp:"Pawan Kumar",vd:"2026-08-23",cu:"NA",cn:"NA",co:"RAHISH ALI",cc:"9990373858",si:"PLOT NO. 761",sa:"IMT KHARKHODA",ar:"25000",gr:"M30",rd:"",rm:"2 FLOOR COMPLETED LABOUR CONT SHEKHAR 8739937374"},
{id:15,sp:"Pawan Kumar",vd:"2026-08-23",cu:"SHAILASH",cn:"",co:"PREM PANDAY",cc:"9210137131",si:"PLOT NO. 320",sa:"IMT KHARKHODA",ar:"2000",gr:"",rd:"",rm:"2 FLOOR COMPLETED LABOUR CONT VAIDNATH 9910764412"},
{id:16,sp:"Pawan Kumar",vd:"2026-08-21",cu:"NA",cn:"NA",co:"ANKUR",cc:"8640000709",si:"SANT KABIR FARM HOUSE",sa:"DELHI ROAD KHARKHODA",ar:"",gr:"M25",rd:"2026-09-03",rm:"REQUIRED RMC 03 SEP 26"},
{id:17,sp:"Pawan Kumar",vd:"2026-08-22",cu:"NA",cn:"NA",co:"NITIN GUPTA",cc:"9871066092",si:"PLOT NO. 2500",sa:"IMT KHARKHODA",ar:"800",gr:"M50",rd:"2026-09-23",rm:"RMC REQUIRED 23-SEP-26"},
{id:18,sp:"Pawan Kumar",vd:"2026-08-22",cu:"NA",cn:"NA",co:"J K DUBEY",cc:"9971769836",si:"PLOT NO. 2503",sa:"IMT KHARKHODA",ar:"800",gr:"M25",rd:"2026-08-28",rm:"LABOUR THEKEDAR TILAK RAJ 7289940157"},
{id:19,sp:"Pawan Kumar",vd:"2026-08-22",cu:"NA",cn:"NA",co:"BIMAL PARSHAD",cc:"7633894798",si:"POWAR HOUSE",sa:"IMT KHARKHODA",ar:"",gr:"M40",rd:"2026-09-02",rm:"SUPERVISOR DHANJAY 9570255627 RMC REQUIRED 08-SEP-26"},
{id:20,sp:"Parvinder Kumar",vd:"2026-08-24",cu:"KEC/Maruti",cn:"7499922442",co:"Mr. Ravi",cc:"7499922442",si:"IMT Kharkhoda",sa:"IMT Kharkhoda",ar:"",gr:"Multiple",rd:"2026-10-01",rm:""}
];
var nRid=21;
var SL=[
  {id:1,nm:"Parvinder Kumar",rl:"Sales Executive",dp:"Sales",ph:"9876543210",em:"parvinder@rmc.com",jd:"2024-01-01",st:"Active",cl:"#1a56db"},
  {id:2,nm:"Pawan Kumar",rl:"Sales Executive",dp:"Sales",ph:"9876543211",em:"pawan@rmc.com",jd:"2024-01-01",st:"Active",cl:"#057a55"}
];
var nSid=3;
var OS=[
  {id:1,nm:"Rajesh Sharma",rl:"Office Manager",dp:"Admin",ph:"9812300001",st:"Active",cl:"#7c3aed"},
  {id:2,nm:"Sunita Devi",rl:"Accounts Executive",dp:"Accounts",ph:"9812300002",st:"Active",cl:"#e02424"},
  {id:3,nm:"Amit Verma",rl:"Data Entry",dp:"Operations",ph:"9812300003",st:"Active",cl:"#f59e0b"}
];
var nOSid=4;
var WL=[
  {id:1,sn:"Rajesh Sharma",dt:"2026-08-24",tk:"Prepare monthly billing report",sts:"Done",pr:"High",nt:"Sent to accounts"},
  {id:2,sn:"Sunita Devi",dt:"2026-08-24",tk:"GST filing for August",sts:"In Progress",pr:"High",nt:"Due today"},
  {id:3,sn:"Amit Verma",dt:"2026-08-24",tk:"Update customer database",sts:"Pending",pr:"Medium",nt:""}
];
var nWid=4;
var FR=[].concat(R),cp=1,PS=10,sf="vd",sd=1,eid=null;

window.addEventListener("DOMContentLoaded",function(){
  document.getElementById("pd").textContent="Generated: "+new Date().toLocaleString("en-IN");
  popDD();applyF();rStats();rStg();rOS();rWL();
});

function fd(d){if(!d||d==="NA")return"\u2014";try{var x=new Date(d);if(isNaN(x))return d;return x.toLocaleDateString("en-IN",{day:"2-digit",month:"short",year:"numeric"});}catch(e){return d;}}
function dl(d){if(!d||d==="NA")return Infinity;var t=new Date();t.setHours(0,0,0,0);var x=new Date(d);x.setHours(0,0,0,0);return Math.round((x-t)/86400000);}
function gc(g){var n=parseInt((g||"").replace(/\\D/g,""))||0;if(n>=40)return"br";if(n>=30)return"by";if(n>=25)return"bb";return"bgy";}
function toast(m,t){var c=document.getElementById("tc2"),el=document.createElement("div");el.className="toast "+(t||"");el.textContent=(t==="success"?"\u2705 ":t==="error"?"\u274C ":"\u2139\uFE0F ")+m;c.appendChild(el);setTimeout(function(){el.remove();},3200);}
function hoc(e){if(e.target===document.getElementById("mo"))closeModal();}
function openModal(){document.getElementById("mo").classList.add("open");}
function closeModal(){document.getElementById("mo").classList.remove("open");eid=null;}
document.addEventListener("keydown",function(e){if(e.key==="Escape")closeModal();});
function swTab(btn,tid){
  document.querySelectorAll(".tp").forEach(function(p){p.classList.remove("act");});
  document.querySelectorAll(".tb").forEach(function(b){b.classList.remove("act");});
  document.getElementById(tid).classList.add("act");btn.classList.add("act");
  if(tid==="tp-2")rUp();if(tid==="tp-5")rAn();if(tid==="tp-3")rStg();
  if(tid==="tp-4"){rOS();rWL();}
}
function popDD(){
  var sps=[].concat(...[R.map(function(r){return r.sp;})]).filter(function(v,i,a){return v&&a.indexOf(v)===i;});
  var grs=R.map(function(r){return r.gr;}).filter(function(v,i,a){return v&&v!=="NA"&&a.indexOf(v)===i;});
  var dts=R.map(function(r){return r.vd;}).filter(function(v,i,a){return v&&a.indexOf(v)===i;}).sort();
  var fsp=document.getElementById("fsp"),fgr=document.getElementById("fgr"),fdt=document.getElementById("fdt");
  fsp.innerHTML="<option value=''>All Salespersons</option>";
  fgr.innerHTML="<option value=''>All Grades</option>";
  fdt.innerHTML="<option value=''>All Dates</option>";
  sps.forEach(function(v){fsp.innerHTML+="<option>"+v+"</option>";});
  grs.forEach(function(v){fgr.innerHTML+="<option>"+v+"</option>";});
  dts.forEach(function(v){fdt.innerHTML+="<option value='"+v+"'>"+fd(v)+"</option>";});
}
function applyF(){
  var q=document.getElementById("srch").value.toLowerCase();
  var sp=document.getElementById("fsp").value,gr=document.getElementById("fgr").value,dt=document.getElementById("fdt").value;
  FR=R.filter(function(r){
    var m=!q||Object.values(r).some(function(v){return String(v).toLowerCase().indexOf(q)>=0;});
    return m&&(!sp||r.sp===sp)&&(!gr||r.gr===gr)&&(!dt||r.vd===dt);
  });
  srtR();cp=1;rTbl();
}
function clrF(){["srch","fsp","fgr","fdt"].forEach(function(id){document.getElementById(id).value="";});applyF();}
function srt(f){if(sf===f)sd*=-1;else{sf=f;sd=1;}srtR();rTbl();}
function srtR(){FR.sort(function(a,b){var av=a[sf]||"",bv=b[sf]||"";if(sf==="ar"){av=parseInt(av)||0;bv=parseInt(bv)||0;}return av<bv?-sd:av>bv?sd:0;});}
function rStats(){
  var ta=R.reduce(function(s,r){return s+(parseInt(r.ar)||0);},0);
  var up=R.filter(function(r){return r.rd&&dl(r.rd)>=0&&dl(r.rd)<=14;}).length;
  document.getElementById("sg").innerHTML=
    "<div class='sc'><div class='sl'>Total Visits</div><div class='sv'>"+R.length+"</div></div>"+
    "<div class='sc a'><div class='sl'>Total Area (sqft)</div><div class='sv'>"+ta.toLocaleString()+"</div></div>"+
    "<div class='sc s'><div class='sl'>Due in 14 Days</div><div class='sv'>"+up+"</div></div>"+
    "<div class='sc pu'><div class='sl'>Sales Staff</div><div class='sv'>"+SL.length+"</div></div>"+
    "<div class='sc d'><div class='sl'>Office Staff</div><div class='sv'>"+OS.length+"</div></div>";
}
function rTbl(){
  var tbody=document.getElementById("tb"),s=(cp-1)*PS,pg=FR.slice(s,s+PS);
  document.getElementById("rc").textContent=FR.length+" record(s)";
  if(!pg.length){tbody.innerHTML="<tr><td colspan='14' class='nd'>No records found.</td></tr>";return;}
  tbody.innerHTML=pg.map(function(r,i){
    return "<tr>"+
      "<td style='color:var(--m);font-size:.75rem'>"+(s+i+1)+"</td>"+
      "<td><span class='badge "+(r.sp.indexOf("Parvinder")>=0?"bb":"bg")+"'>"+r.sp+"</span></td>"+
      "<td>"+fd(r.vd)+"</td>"+
      "<td>"+(r.cu&&r.cu!=="NA"?r.cu:"\u2014")+"</td>"+
      "<td>"+(r.cn&&r.cn!=="NA"?"<a href='tel:"+r.cn+"'>"+r.cn+"</a>":"\u2014")+"</td>"+
      "<td><strong>"+(r.co||"\u2014")+"</strong></td>"+
      "<td>"+(r.cc?"<a href='tel:"+r.cc+"'>"+r.cc+"</a>":"\u2014")+"</td>"+
      "<td>"+(r.si||"\u2014")+"</td>"+
      "<td style='max-width:120px;font-size:.77rem'>"+(r.sa||"\u2014")+"</td>"+
      "<td>"+(r.ar?Number(r.ar).toLocaleString():"\u2014")+"</td>"+
      "<td>"+(r.gr?"<span class='badge "+gc(r.gr)+"'>"+r.gr+"</span>":"\u2014")+"</td>"+
      "<td style='color:"+(r.rd&&dl(r.rd)<7?"var(--d)":"inherit")+"'>"+(r.rd?fd(r.rd):"<span style='color:var(--m)'>TBD</span>")+"</td>"+
      "<td style='max-width:170px;font-size:.76rem'>"+(r.rm||"\u2014")+"</td>"+
      "<td><div class='ra'>"+
        "<button class='ib' onclick='vRec("+r.id+")'>&#128065;&#65039;</button>"+
        "<button class='ib' onclick='edV("+r.id+")'>&#9999;&#65039;</button>"+
        "<button class='ib' onclick='delR("+r.id+")'>&#128465;&#65039;</button>"+
      "</div></td></tr>";
  }).join("");
  rPag();
}
function rPag(){
  var tot=Math.ceil(FR.length/PS),bar=document.getElementById("pgb");
  if(tot<=1){bar.innerHTML="";return;}
  var s=(cp-1)*PS+1,e=Math.min(cp*PS,FR.length);
  var h="<span class='pi'>Showing "+s+"\u2013"+e+" of "+FR.length+"</span><div class='pbs'>";
  h+="<button class='pb' onclick='gp("+(cp-1)+")' "+(cp===1?"disabled":"")+">&#8249;</button>";
  for(var p=1;p<=tot;p++){
    if(tot>7&&p>2&&p<tot-1&&Math.abs(p-cp)>1){if(p===3||p===tot-2)h+="<span style='padding:5px 3px'>&#8230;</span>";continue;}
    h+="<button class='pb "+(p===cp?"act":"")+"' onclick='gp("+p+")'>"+p+"</button>";
  }
  h+="<button class='pb' onclick='gp("+(cp+1)+")' "+(cp===tot?"disabled":"")+">&#8250;</button></div>";
  bar.innerHTML=h;
}
function gp(p){var tot=Math.ceil(FR.length/PS);if(p<1||p>tot)return;cp=p;rTbl();}
function rUp(){
  var rows=R.filter(function(r){return r.rd&&r.rd!=="NA";}).map(function(r){return Object.assign({},r,{days:dl(r.rd)});}).filter(function(r){return r.days>=-30;}).sort(function(a,b){return a.days-b.days;});
  var tbody=document.getElementById("utb");
  if(!rows.length){tbody.innerHTML="<tr><td colspan='9' class='nd'>No upcoming.</td></tr>";return;}
  tbody.innerHTML=rows.map(function(r){
    var bg=r.days<0?"br":r.days<=3?"br":r.days<=7?"by":"bg";
    var lb=r.days>=0?r.days+" days":Math.abs(r.days)+"d ago";
    return "<tr><td>"+r.sp+"</td><td>"+(r.cu&&r.cu!=="NA"?r.cu:"\u2014")+"</td><td>"+r.co+"</td><td>"+r.si+"</td>"+
      "<td>"+(r.ar?Number(r.ar).toLocaleString():"\u2014")+"</td>"+
      "<td>"+(r.gr?"<span class='badge "+gc(r.gr)+"'>"+r.gr+"</span>":"\u2014")+"</td>"+
      "<td>"+fd(r.rd)+"</td><td><span class='badge "+bg+"'>"+lb+"</span></td>"+
      "<td style='font-size:.77rem'>"+(r.rm||"\u2014")+"</td></tr>";
  }).join("");
}
function rStg(){
  var g=document.getElementById("stgr");
  if(!SL.length){g.innerHTML="<div class='nd' style='padding:28px'>No staff added.</div>";return;}
  var ac=["#1a56db","#057a55","#7c3aed","#e02424","#f59e0b","#0891b2","#be185d"];
  g.innerHTML=SL.map(function(s,i){
    return "<div class='scard'>"+
      "<div class='sca'><button class='ib' onclick='edSt("+s.id+")'>&#9999;&#65039;</button><button class='ib' onclick='delSt("+s.id+")'>&#128465;&#65039;</button></div>"+
      "<div class='stop'><div class='sav' style='background:"+(s.cl||ac[i%ac.length])+"'>"+s.nm.charAt(0)+"</div>"+
      "<div><div class='snm'>"+s.nm+"</div><div class='srl'>"+s.rl+"</div></div></div>"+
      "<span class='badge "+(s.dp==="Sales"?"bb":"bg")+"'>"+s.dp+"</span>"+
      "<div class='sdt'>&#128222; "+(s.ph||"\u2014")+"</div>"+
      "<div class='sdt'>&#9993;&#65039; "+(s.em||"\u2014")+"</div>"+
      "<div class='sdt'>&#128197; Joined: "+fd(s.jd)+"</div>"+
      "<span class='badge "+(s.st==="Active"?"bg":"br")+"'>"+s.st+"</span></div>";
  }).join("");
}
function rOS(){
  var el=document.getElementById("osl");
  if(!OS.length){el.innerHTML="<div class='nd' style='padding:14px'>No office staff.</div>";return;}
  el.innerHTML=OS.map(function(s){
    return "<div style='display:flex;align-items:center;justify-content:space-between;background:#f8fafc;border:1.5px solid var(--b);border-radius:8px;padding:9px 11px'>"+
      "<div style='display:flex;align-items:center;gap:9px'>"+
      "<div style='width:35px;height:35px;border-radius:50%;background:"+(s.cl||"#7c3aed")+";color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.95rem'>"+s.nm.charAt(0)+"</div>"+
      "<div><div style='font-weight:700;font-size:.88rem'>"+s.nm+"</div>"+
      "<div style='font-size:.74rem;color:var(--m)'>"+s.rl+" &middot; "+s.dp+"</div>"+
      "<div style='font-size:.74rem;color:var(--m)'>&#128222; "+s.ph+"</div></div></div>"+
      "<div style='display:flex;align-items:center;gap:5px'>"+
      "<span class='badge "+(s.st==="Active"?"bg":"br")+"'>"+s.st+"</span>"+
      "<button class='ib' onclick='edOS("+s.id+")'>&#9999;&#65039;</button>"+
      "<button class='ib' onclick='delOS("+s.id+")'>&#128465;&#65039;</button></div></div>";
  }).join("");
}
function rWL(){
  var tb=document.getElementById("wlb");
  if(!WL.length){tb.innerHTML="<tr><td colspan='8' class='nd'>No work entries.</td></tr>";return;}
  tb.innerHTML=WL.map(function(w,i){
    var sc=w.sts==="Done"?"bg":w.sts==="In Progress"?"by":"bgy";
    var pc=w.pr==="High"?"br":w.pr==="Medium"?"bor":"bb";
    return "<tr><td style='color:var(--m);font-size:.75rem'>"+(i+1)+"</td>"+
      "<td><strong>"+w.sn+"</strong></td><td>"+fd(w.dt)+"</td><td>"+w.tk+"</td>"+
      "<td><span class='badge "+sc+"'>"+w.sts+"</span></td>"+
      "<td><span class='badge "+pc+"'>"+w.pr+"</span></td>"+
      "<td style='font-size:.77rem'>"+(w.nt||"\u2014")+"</td>"+
      "<td><div class='ra'>"+
        "<button class='ib' onclick='edWL("+w.id+")'>&#9999;&#65039;</button>"+
        "<button class='ib' onclick='delWL("+w.id+")'>&#128465;&#65039;</button>"+
      "</div></td></tr>";
  }).join("");
}
function rAn(){
  var bsp={};R.forEach(function(r){if(!bsp[r.sp])bsp[r.sp]={c:0,a:0};bsp[r.sp].c++;bsp[r.sp].a+=parseInt(r.ar)||0;});
  document.getElementById("an1").innerHTML=Object.keys(bsp).map(function(k){return"<tr><td>"+k+"</td><td>"+bsp[k].c+"</td><td>"+bsp[k].a.toLocaleString()+" sqft</td></tr>";}).join("");
  var bgr={};R.forEach(function(r){if(r.gr&&r.gr!=="NA")bgr[r.gr]=(bgr[r.gr]||0)+1;});
  var tot=Object.values(bgr).reduce(function(s,v){return s+v;},0)||1;
  document.getElementById("an2").innerHTML=Object.keys(bgr).sort(function(a,b){return bgr[b]-bgr[a];}).map(function(g){return"<tr><td><span class='badge "+gc(g)+"'>"+g+"</span></td><td>"+bgr[g]+"</td><td>"+Math.round(bgr[g]/tot*100)+"%</td></tr>";}).join("");
  var bdp={};SL.concat(OS).forEach(function(s){bdp[s.dp]=(bdp[s.dp]||0)+1;});
  document.getElementById("an3").innerHTML=Object.keys(bdp).map(function(k){return"<tr><td>"+k+"</td><td>"+bdp[k]+"</td></tr>";}).join("");
}

// ===== FORMS =====
function sfHTML(s){s=s||{};
  var dr=["Sales","Operations","Accounts","Admin","HR","Technical","Other"];
  var rl=["Sales Executive","Sales Manager","Area Manager","Operations","Accounts","Admin","HR","Batch Plant Operator","QC Engineer","Driver","Other"];
  return "<div class='fg'>"+
    "<div class='fi'><label>Full Name *</label><input id='sfn' value='"+(s.nm||"")+"' placeholder='Staff full name'></div>"+
    "<div class='fi'><label>Role *</label><select id='sfr'>"+rl.map(function(r){return"<option "+(s.rl===r?"selected":"")+">"+r+"</option>";}).join("")+"</select></div>"+
    "<div class='fi'><label>Department</label><select id='sfd'>"+dr.map(function(d){return"<option "+(s.dp===d?"selected":"")+">"+d+"</option>";}).join("")+"</select></div>"+
    "<div class='fi'><label>Phone</label><input id='sfp' value='"+(s.ph||"")+"' placeholder='Mobile number'></div>"+
    "<div class='fi'><label>Email</label><input id='sfe' value='"+(s.em||"")+"' placeholder='Email address'></div>"+
    "<div class='fi'><label>Join Date</label><input id='sfj' type='date' value='"+(s.jd||"")+"'></div>"+
    "<div class='fi'><label>Status</label><select id='sfs'><option "+(s.st==="Active"?"selected":"")+">Active</option><option "+(s.st==="Inactive"?"selected":"")+">Inactive</option></select></div>"+
    "<div class='fi'><label>Avatar Color</label><input id='sfc' type='color' value='"+(s.cl||"#1a56db")+"' style='height:37px;padding:2px'></div></div>";
}
function openAddStaffModal(){eid=null;document.getElementById("mt").textContent="\uD83D\uDC64 Add New Staff";document.getElementById("mb2").innerHTML=sfHTML();document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Cancel</button><button class='btn bp' onclick='saveSt()'>\uD83D\uDCBE Save Staff</button>";openModal();}
function edSt(id){var s=SL.filter(function(x){return x.id===id;})[0];if(!s)return;eid=id;document.getElementById("mt").textContent="\u270F\uFE0F Edit Staff";document.getElementById("mb2").innerHTML=sfHTML(s);document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Cancel</button><button class='btn bp' onclick='saveSt()'>\uD83D\uDCBE Update Staff</button>";openModal();}
function saveSt(){var nm=document.getElementById("sfn").value.trim();if(!nm){toast("Enter staff name","error");return;}var d={nm:nm,rl:document.getElementById("sfr").value,dp:document.getElementById("sfd").value,ph:document.getElementById("sfp").value.trim(),em:document.getElementById("sfe").value.trim(),jd:document.getElementById("sfj").value,st:document.getElementById("sfs").value,cl:document.getElementById("sfc").value};if(eid){var ix=SL.map(function(x){return x.id;}).indexOf(eid);SL[ix]=Object.assign({},SL[ix],d);toast("Staff updated!","success");}else{d.id=nSid++;SL.push(d);toast("Staff added!","success");}closeModal();rStg();rStats();rAn();popDD();}
function delSt(id){if(!confirm("Delete this staff?"))return;SL=SL.filter(function(s){return s.id!==id;});rStg();rStats();toast("Staff deleted.","error");}

function osHTML(s){s=s||{};
  var dr=["Admin","Accounts","Operations","HR","IT","Dispatch","Purchase","Other"];
  var rl=["Office Manager","Accounts Executive","Data Entry","Receptionist","HR Executive","IT Support","Dispatch Officer","Purchase Officer","Office Boy","Other"];
  return "<div class='fg'>"+
    "<div class='fi'><label>Full Name *</label><input id='ofn' value='"+(s.nm||"")+"' placeholder='Staff name'></div>"+
    "<div class='fi'><label>Role *</label><select id='ofr'>"+rl.map(function(r){return"<option "+(s.rl===r?"selected":"")+">"+r+"</option>";}).join("")+"</select></div>"+
    "<div class='fi'><label>Department</label><select id='ofd'>"+dr.map(function(d){return"<option "+(s.dp===d?"selected":"")+">"+d+"</option>";}).join("")+"</select></div>"+
    "<div class='fi'><label>Phone</label><input id='ofp' value='"+(s.ph||"")+"' placeholder='Mobile number'></div>"+
    "<div class='fi'><label>Status</label><select id='ofs'><option "+(s.st==="Active"?"selected":"")+">Active</option><option "+(s.st==="Inactive"?"selected":"")+">Inactive</option></select></div>"+
    "<div class='fi'><label>Avatar Color</label><input id='ofc' type='color' value='"+(s.cl||"#7c3aed")+"' style='height:37px;padding:2px'></div></div>";
}
function openAddOSModal(){eid=null;document.getElementById("mt").textContent="\uD83D\uDC64 Add Office Staff";document.getElementById("mb2").innerHTML=osHTML();document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Cancel</button><button class='btn bp' onclick='saveOS()'>\uD83D\uDCBE Save</button>";openModal();}
function edOS(id){var s=OS.filter(function(x){return x.id===id;})[0];if(!s)return;eid=id;document.getElementById("mt").textContent="\u270F\uFE0F Edit Office Staff";document.getElementById("mb2").innerHTML=osHTML(s);document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Cancel</button><button class='btn bp' onclick='saveOS()'>\uD83D\uDCBE Update</button>";openModal();}
function saveOS(){var nm=document.getElementById("ofn").value.trim();if(!nm){toast("Enter staff name","error");return;}var d={nm:nm,rl:document.getElementById("ofr").value,dp:document.getElementById("ofd").value,ph:document.getElementById("ofp").value.trim(),st:document.getElementById("ofs").value,cl:document.getElementById("ofc").value};if(eid){var ix=OS.map(function(x){return x.id;}).indexOf(eid);OS[ix]=Object.assign({},OS[ix],d);toast("Updated!","success");}else{d.id=nOSid++;OS.push(d);toast("Office staff added!","success");}closeModal();rOS();rStats();rAn();}
function delOS(id){if(!confirm("Delete?"))return;OS=OS.filter(function(s){return s.id!==id;});rOS();rStats();toast("Deleted.","error");}

function wlHTML(w){w=w||{};
  var all=OS.concat(SL);
  return "<div class='fg'>"+
    "<div class='fi'><label>Staff Member *</label><select id='wfs'><option value=''>-- Select Staff --</option>"+
    all.map(function(s){return"<option value='"+s.nm+"' "+(w.sn===s.nm?"selected":"")+">"+s.nm+" ("+s.dp+")</option>";}).join("")+"</select></div>"+
    "<div class='fi'><label>Date *</label><input id='wfd' type='date' value='"+(w.dt||new Date().toISOString().slice(0,10))+"'></div>"+
    "<div class='fi full'><label>Task / Work Description *</label><input id='wft' value='"+(w.tk||"")+"' placeholder='Describe the task clearly'></div>"+
    "<div class='fi'><label>Status</label><select id='wfst'><option "+(w.sts==="Pending"?"selected":"")+">Pending</option><option "+(w.sts==="In Progress"?"selected":"")+">In Progress</option><option "+(w.sts==="Done"?"selected":"")+">Done</option><option "+(w.sts==="On Hold"?"selected":"")+">On Hold</option></select></div>"+
    "<div class='fi'><label>Priority</label><select id='wfp'><option "+(w.pr==="High"?"selected":"")+">High</option><option "+(w.pr==="Medium"?"selected":"")+">Medium</option><option "+(w.pr==="Low"?"selected":"")+">Low</option></select></div>"+
    "<div class='fi full'><label>Notes</label><textarea id='wfn'>"+(w.nt||"")+"</textarea></div></div>";
}
function openAddWLModal(){eid=null;document.getElementById("mt").textContent="\u2795 Add Work Entry";document.getElementById("mb2").innerHTML=wlHTML();document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Cancel</button><button class='btn bs' onclick='saveWL()'>\uD83D\uDCBE Save Entry</button>";openModal();}
function edWL(id){var w=WL.filter(function(x){return x.id===id;})[0];if(!w)return;eid=id;document.getElementById("mt").textContent="\u270F\uFE0F Edit Work Entry";document.getElementById("mb2").innerHTML=wlHTML(w);document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Cancel</button><button class='btn bs' onclick='saveWL()'>\uD83D\uDCBE Update Entry</button>";openModal();}
function saveWL(){var sn=document.getElementById("wfs").value,tk=document.getElementById("wft").value.trim(),dt=document.getElementById("wfd").value;if(!sn||!tk||!dt){toast("Fill Staff, Task and Date","error");return;}var d={sn:sn,dt:dt,tk:tk,sts:document.getElementById("wfst").value,pr:document.getElementById("wfp").value,nt:document.getElementById("wfn").value.trim()};if(eid){var ix=WL.map(function(x){return x.id;}).indexOf(eid);WL[ix]=Object.assign({},WL[ix],d);toast("Updated!","success");}else{d.id=nWid++;WL.push(d);toast("Work entry added!","success");}closeModal();rWL();}
function delWL(id){if(!confirm("Delete?"))return;WL=WL.filter(function(w){return w.id!==id;});rWL();toast("Deleted.","error");}

function vfHTML(r){r=r||{};
  var gr=["M10","M15","M20","M25","M30","M35","M40","M45","M50","M10/M30","Multiple"];
  var allsp=SL.map(function(s){return s.nm;}).concat(["Parvinder Kumar","Pawan Kumar"]).filter(function(v,i,a){return a.indexOf(v)===i;});
  return "<div class='fg'>"+
    "<div class='fi'><label>Salesperson *</label><select id='vfsp'><option value=''>-- Select --</option>"+allsp.map(function(n){return"<option "+(r.sp===n?"selected":"")+">"+n+"</option>";}).join("")+"<option value='__o__'>Other...</option></select></div>"+
    "<div class='fi'><label>Custom Salesperson</label><input id='vfc' placeholder='If not in list'></div>"+
    "<div class='fi'><label>Visit Date *</label><input id='vfd' type='date' value='"+(r.vd||"")+"'></div>"+
    "<div class='fi'><label>Customer</label><input id='vfcu' value='"+(r.cu&&r.cu!=="NA"?r.cu:"")+"' placeholder='Customer name'></div>"+
    "<div class='fi'><label>Customer Contact</label><input id='vfcn' value='"+(r.cn&&r.cn!=="NA"?r.cn:"")+"' placeholder='Phone'></div>"+
    "<div class='fi'><label>Contractor *</label><input id='vfco' value='"+(r.co||"")+"' placeholder='Contractor name'></div>"+
    "<div class='fi'><label>Contractor Contact</label><input id='vfcc' value='"+(r.cc||"")+"' placeholder='Phone'></div>"+
    "<div class='fi'><label>Site / Project</label><input id='vfsi' value='"+(r.si||"")+"' placeholder='Site name'></div>"+
    "<div class='fi'><label>Site Address</label><input id='vfsa' value='"+(r.sa||"")+"' placeholder='Full address'></div>"+
    "<div class='fi'><label>Total Area (sqft)</label><input id='vfar' type='number' value='"+(r.ar||"")+"' placeholder='e.g. 2500'></div>"+
    "<div class='fi'><label>Concrete Grade</label><select id='vfgr'><option value=''>-- Select --</option>"+gr.map(function(g){return"<option "+(r.gr===g?"selected":"")+">"+g+"</option>";}).join("")+"<option value='custom'>Custom</option></select></div>"+
    "<div class='fi'><label>Custom Grade</label><input id='vfgc' value='"+(gr.indexOf(r.gr)<0?(r.gr||""):"")+"' placeholder='e.g. M55'></div>"+
    "<div class='fi'><label>Required Date</label><input id='vfrd' type='date' value='"+(r.rd||"")+"'></div>"+
    "<div class='fi full'><label>Remarks</label><textarea id='vfrm'>"+(r.rm||"")+"</textarea></div></div>";
}
function openAddVisitModal(){eid=null;document.getElementById("mt").textContent="\u2795 Add New Visit";document.getElementById("mb2").innerHTML=vfHTML();document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Cancel</button><button class='btn bw' style='background:var(--p);color:#fff' onclick='saveV()'>\uD83D\uDCBE Save Visit</button>";openModal();}
function edV(id){var r=R.filter(function(x){return x.id===id;})[0];if(!r)return;eid=id;document.getElementById("mt").textContent="\u270F\uFE0F Edit Visit";document.getElementById("mb2").innerHTML=vfHTML(r);document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Cancel</button><button class='btn bw' style='background:var(--p);color:#fff' onclick='saveV()'>\uD83D\uDCBE Update Visit</button>";openModal();}
function saveV(){var spv=document.getElementById("vfsp").value,spc=document.getElementById("vfc").value.trim(),sp=spv==="__o__"?spc:spv,vd=document.getElementById("vfd").value,co=document.getElementById("vfco").value.trim();if(!sp||!vd||!co){toast("Fill Salesperson, Visit Date & Contractor","error");return;}var grv=document.getElementById("vfgr").value,grc=document.getElementById("vfgc").value.trim(),gr=grv==="custom"?grc:grv;var d={sp:sp,vd:vd,cu:document.getElementById("vfcu").value.trim()||"NA",cn:document.getElementById("vfcn").value.trim()||"NA",co:co,cc:document.getElementById("vfcc").value.trim(),si:document.getElementById("vfsi").value.trim(),sa:document.getElementById("vfsa").value.trim(),ar:document.getElementById("vfar").value.trim(),gr:gr,rd:document.getElementById("vfrd").value,rm:document.getElementById("vfrm").value.trim()};if(eid){var ix=R.map(function(x){return x.id;}).indexOf(eid);R[ix]=Object.assign({},R[ix],d);toast("Visit updated!","success");}else{d.id=nRid++;R.unshift(d);toast("Visit added!","success");}closeModal();popDD();applyF();rStats();}
function vRec(id){var r=R.filter(function(x){return x.id===id;})[0];if(!r)return;document.getElementById("mt").textContent="\uD83D\uDC41\uFE0F Visit Details";document.getElementById("mb2").innerHTML="<div class='dg'><div class='di'><label>Salesperson</label><div class='val'><span class='badge bb'>"+r.sp+"</span></div></div><div class='di'><label>Visit Date</label><div class='val'>"+fd(r.vd)+"</div></div><div class='di'><label>Customer</label><div class='val'>"+(r.cu&&r.cu!=="NA"?r.cu:"\u2014")+"</div></div><div class='di'><label>Customer Contact</label><div class='val'>"+(r.cn&&r.cn!=="NA"?"<a href='tel:"+r.cn+"'>"+r.cn+"</a>":"\u2014")+"</div></div><div class='di'><label>Contractor</label><div class='val'><strong>"+r.co+"</strong></div></div><div class='di'><label>Contractor No.</label><div class='val'>"+(r.cc?"<a href='tel:"+r.cc+"'>"+r.cc+"</a>":"\u2014")+"</div></div><div class='di'><label>Site</label><div class='val'>"+(r.si||"\u2014")+"</div></div><div class='di'><label>Address</label><div class='val'>"+(r.sa||"\u2014")+"</div></div><div class='di'><label>Total Area</label><div class='val'>"+(r.ar?Number(r.ar).toLocaleString()+" sqft":"\u2014")+"</div></div><div class='di'><label>Grade</label><div class='val'>"+(r.gr?"<span class='badge "+gc(r.gr)+"'>"+r.gr+"</span>":"\u2014")+"</div></div><div class='di'><label>Required Date</label><div class='val'>"+(r.rd?fd(r.rd):"TBD")+"</div></div><div class='di'><label>Days Remaining</label><div class='val'>"+(r.rd?dl(r.rd)+" days":"\u2014")+"</div></div><div class='di full'><label>Remarks</label><div class='val' style='background:#f8fafc;padding:9px;border-radius:7px'>"+(r.rm||"\u2014")+"</div></div></div>";document.getElementById("mf2").innerHTML="<button class='btn bo' onclick='closeModal()'>Close</button><button class='btn bw' style='background:var(--p);color:#fff' onclick='closeModal();edV("+r.id+")'>\u270F\uFE0F Edit</button>";openModal();}
function delR(id){if(!confirm("Delete this visit?"))return;R=R.filter(function(r){return r.id!==id;});applyF();rStats();toast("Deleted.","error");}

function expCSV(){var h=["ID","Salesperson","Visit Date","Customer","Contact","Contractor","Cont No","Site","Address","Area","Grade","Req Date","Remarks"];var rows=FR.map(function(r){return[r.id,r.sp,r.vd,r.cu,r.cn,r.co,r.cc,r.si,r.sa,r.ar,r.gr,r.rd,'"'+(r.rm||"").replace(/"/g,'""')+'"'];});var csv=[h].concat(rows).map(function(r){return r.join(",");}).join("\\n");var a=document.createElement("a");a.href=URL.createObjectURL(new Blob([csv],{type:"text/csv"}));a.download="RMC_Sales_"+new Date().toISOString().slice(0,10)+".csv";a.click();toast("CSV exported!","success");}

function exportPDF(){
  try{
    var jsPDF=window.jspdf.jsPDF;
    var doc=new jsPDF({orientation:"landscape",unit:"mm",format:"a4"});
    doc.setFillColor(26,86,219);doc.rect(0,0,297,20,"F");
    doc.setTextColor(255,255,255);doc.setFontSize(13);doc.setFont("helvetica","bold");
    doc.text("RMC Sales Visit Report",14,9);
    doc.setFontSize(8);doc.setFont("helvetica","normal");
    doc.text("Ready-Mix Concrete Sales Management System",14,15);
    doc.text("Generated: "+new Date().toLocaleString("en-IN"),180,9);
    doc.text("Records: "+FR.length,180,15);
    doc.setTextColor(0,0,0);
    doc.autoTable({
      head:[["#","Salesperson","Date","Customer","Contractor","Cont.No.","Site","Address","Area","Grade","Req.Date","Remarks"]],
      body:FR.map(function(r,i){return[i+1,r.sp,fd(r.vd),r.cu!=="NA"?r.cu:"\u2014",r.co,r.cc||"\u2014",r.si||"\u2014",r.sa||"\u2014",r.ar?Number(r.ar).toLocaleString():"\u2014",r.gr||"\u2014",r.rd?fd(r.rd):"TBD",(r.rm||"\u2014").substring(0,55)];}),
      startY:23,styles:{fontSize:7,cellPadding:2},
      headStyles:{fillColor:[26,86,219],textColor:255,fontStyle:"bold"},
      alternateRowStyles:{fillColor:[248,250,252]},margin:{left:12,right:12}
    });
    var upc=R.filter(function(r){return r.rd&&dl(r.rd)>=0&&dl(r.rd)<=30;}).sort(function(a,b){return dl(a.rd)-dl(b.rd);});
    if(upc.length){
      doc.addPage();doc.setFillColor(5,122,85);doc.rect(0,0,297,20,"F");
      doc.setTextColor(255,255,255);doc.setFontSize(12);doc.setFont("helvetica","bold");
      doc.text("Upcoming Requirements \u2014 Next 30 Days",14,13);doc.setTextColor(0,0,0);
      doc.autoTable({head:[["Salesperson","Customer","Contractor","Site","Area","Grade","Required Date","Days Left","Remarks"]],
        body:upc.map(function(r){return[r.sp,r.cu!=="NA"?r.cu:"\u2014",r.co,r.si,r.ar?Number(r.ar).toLocaleString():"\u2014",r.gr||"\u2014",fd(r.rd),dl(r.rd)+" days",(r.rm||"\u2014").substring(0,50)];}),
        startY:23,styles:{fontSize:7.5,cellPadding:2},headStyles:{fillColor:[5,122,85],textColor:255,fontStyle:"bold"},alternateRowStyles:{fillColor:[240,253,244]},margin:{left:12,right:12}});
    }
    doc.addPage();doc.setFillColor(124,58,237);doc.rect(0,0,297,20,"F");
    doc.setTextColor(255,255,255);doc.setFontSize(12);doc.setFont("helvetica","bold");
    doc.text("Staff Directory",14,13);doc.setTextColor(0,0,0);
    doc.autoTable({head:[["#","Name","Role","Department","Phone","Email","Status"]],
      body:SL.concat(OS).map(function(s,i){return[i+1,s.nm,s.rl,s.dp,s.ph||"\u2014",s.em||"\u2014",s.st];}),
      startY:23,styles:{fontSize:8,cellPadding:2},headStyles:{fillColor:[124,58,237],textColor:255,fontStyle:"bold"},alternateRowStyles:{fillColor:[250,245,255]},margin:{left:12,right:12}});
    if(WL.length){
      doc.addPage();doc.setFillColor(245,158,11);doc.rect(0,0,297,20,"F");
      doc.setTextColor(255,255,255);doc.setFontSize(12);doc.setFont("helvetica","bold");
      doc.text("Office Staff Work Log",14,13);doc.setTextColor(0,0,0);
      doc.autoTable({head:[["#","Staff","Date","Task","Status","Priority","Notes"]],
        body:WL.map(function(w,i){return[i+1,w.sn,fd(w.dt),w.tk,w.sts,w.pr,w.nt||"\u2014"];}),
        startY:23,styles:{fontSize:8,cellPadding:2},headStyles:{fillColor:[245,158,11],textColor:255,fontStyle:"bold"},alternateRowStyles:{fillColor:[255,251,235]},margin:{left:12,right:12}});
    }
    var pg=doc.internal.getNumberOfPages();
    for(var i=1;i<=pg;i++){doc.setPage(i);doc.setFontSize(7.5);doc.setTextColor(130);doc.text("Page "+i+" of "+pg,148,doc.internal.pageSize.height-5,{align:"center"});doc.text("RMC Sales Management System \u2014 Confidential",12,doc.internal.pageSize.height-5);}
    doc.save("RMC_Report_"+new Date().toISOString().slice(0,10)+".pdf");
    toast("PDF downloaded!","success");
  }catch(e){toast("PDF error: "+e.message,"error");console.error(e);}
}
</script>
</body>
</html>""")

html = "".join(html_parts)
with open("index.html", "w", encoding="utf-8", errors="replace") as f:
    f.write(html)
print("Done! Written", len(html), "bytes")
